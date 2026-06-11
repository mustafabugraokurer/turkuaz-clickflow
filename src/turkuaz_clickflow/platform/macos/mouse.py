"""macOS mouse click adapter."""

from __future__ import annotations

import ctypes
import sys
from dataclasses import dataclass
from typing import Protocol

from turkuaz_clickflow.platform.interfaces import PlatformOperationError


@dataclass(frozen=True)
class MacOSPoint:
    """Mouse position used by the macOS backend."""

    x: float
    y: float


class MacOSMouseBackend(Protocol):
    """Backend contract for one low-level macOS left click."""

    def left_click(self) -> None:
        """Perform the low-level left click operation."""


class MacOSQuartzApi(Protocol):
    """Minimal Quartz API surface used by the backend."""

    def is_process_trusted(self) -> bool:
        """Return whether the process can post accessibility events."""

    def current_mouse_location(self) -> MacOSPoint:
        """Return the current mouse cursor location."""

    def create_mouse_event(self, event_type: int, point: MacOSPoint, button: int):
        """Create a Quartz mouse event."""

    def post_event(self, event) -> None:
        """Post a Quartz event."""

    def release_event(self, event) -> None:
        """Release a Quartz event."""


class MacOSMouseClickAdapter:
    """Mouse click adapter for macOS."""

    def __init__(self, backend: MacOSMouseBackend) -> None:
        self._backend = backend

    def left_click(self) -> None:
        """Perform one left click through the configured backend."""
        try:
            self._backend.left_click()
        except PlatformOperationError as exc:
            raise PlatformOperationError(str(exc)) from exc
        except Exception as exc:
            raise PlatformOperationError(f"macOS left click failed: {exc}") from exc


class UnavailableMacOSMouseBackend:
    """Backend used when macOS mouse APIs are not available."""

    def left_click(self) -> None:
        raise PlatformOperationError("macOS mouse API is not available")


class MacOSQuartzMouseBackend:
    """Real macOS backend using Quartz mouse events."""

    LEFT_MOUSE_DOWN = 1
    LEFT_MOUSE_UP = 2
    LEFT_MOUSE_BUTTON = 0

    def __init__(self, api: MacOSQuartzApi) -> None:
        self._api = api

    def left_click(self) -> None:
        if not self._api.is_process_trusted():
            raise PlatformOperationError(
                "macOS Accessibility or Input Monitoring permission is required "
                "to post mouse events"
            )

        point = self._api.current_mouse_location()
        down_event = self._api.create_mouse_event(
            self.LEFT_MOUSE_DOWN,
            point,
            self.LEFT_MOUSE_BUTTON,
        )
        up_event = self._api.create_mouse_event(
            self.LEFT_MOUSE_UP,
            point,
            self.LEFT_MOUSE_BUTTON,
        )

        try:
            self._api.post_event(down_event)
            self._api.post_event(up_event)
        finally:
            self._api.release_event(down_event)
            self._api.release_event(up_event)


class QuartzPoint(ctypes.Structure):
    """ctypes representation of CGPoint."""

    _fields_ = [
        ("x", ctypes.c_double),
        ("y", ctypes.c_double),
    ]


class MacOSQuartzCtypesApi:
    """ctypes wrapper around macOS ApplicationServices Quartz APIs."""

    EVENT_TAP = 0

    def __init__(self, application_services=None) -> None:
        if application_services is None:
            if sys.platform != "darwin":
                raise PlatformOperationError("macOS mouse API is not available")
            application_services = ctypes.cdll.LoadLibrary(
                "/System/Library/Frameworks/ApplicationServices.framework/"
                "ApplicationServices"
            )
        self._api = application_services
        self._configure_signatures()

    def is_process_trusted(self) -> bool:
        return bool(self._api.AXIsProcessTrusted())

    def current_mouse_location(self) -> MacOSPoint:
        event = self._api.CGEventCreate(None)
        if not event:
            raise PlatformOperationError("Could not read current mouse location")
        try:
            point = self._api.CGEventGetLocation(event)
            return MacOSPoint(point.x, point.y)
        finally:
            self.release_event(event)

    def create_mouse_event(self, event_type: int, point: MacOSPoint, button: int):
        event = self._api.CGEventCreateMouseEvent(
            None,
            event_type,
            QuartzPoint(point.x, point.y),
            button,
        )
        if not event:
            raise PlatformOperationError("Could not create macOS mouse event")
        return event

    def post_event(self, event) -> None:
        try:
            self._api.CGEventPost(self.EVENT_TAP, event)
        except Exception as exc:
            raise PlatformOperationError(
                "macOS Quartz could not post mouse event; Accessibility or "
                "Input Monitoring permission may be required"
            ) from exc

    def release_event(self, event) -> None:
        self._api.CFRelease(event)

    def _configure_signatures(self) -> None:
        self._api.AXIsProcessTrusted.restype = ctypes.c_bool
        self._api.CGEventCreate.argtypes = [ctypes.c_void_p]
        self._api.CGEventCreate.restype = ctypes.c_void_p
        self._api.CGEventGetLocation.argtypes = [ctypes.c_void_p]
        self._api.CGEventGetLocation.restype = QuartzPoint
        self._api.CGEventCreateMouseEvent.argtypes = [
            ctypes.c_void_p,
            ctypes.c_uint32,
            QuartzPoint,
            ctypes.c_uint32,
        ]
        self._api.CGEventCreateMouseEvent.restype = ctypes.c_void_p
        self._api.CGEventPost.argtypes = [ctypes.c_uint32, ctypes.c_void_p]
        self._api.CGEventPost.restype = None
        self._api.CFRelease.argtypes = [ctypes.c_void_p]
        self._api.CFRelease.restype = None


def create_macos_mouse_backend() -> MacOSMouseBackend:
    """Create the real macOS mouse backend when available."""
    if sys.platform != "darwin":
        return UnavailableMacOSMouseBackend()
    return MacOSQuartzMouseBackend(MacOSQuartzCtypesApi())
