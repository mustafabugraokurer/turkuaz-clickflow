"""macOS global hotkey adapter."""

from __future__ import annotations

import ctypes
import logging
import sys
import threading
import time
from dataclasses import dataclass
from typing import Callable, Dict, Optional, Protocol

from turkuaz_clickflow.platform.interfaces import PlatformOperationError


logger = logging.getLogger(__name__)


class MacOSHotkeyBackend(Protocol):
    """Backend contract for macOS global hotkey registration."""

    def register(
        self,
        hotkey_id: int,
        key_code: int,
        callback: Callable[[], None],
    ) -> None:
        """Register a low-level macOS hotkey."""

    def unregister(self, hotkey_id: int) -> None:
        """Unregister a low-level macOS hotkey."""


@dataclass(frozen=True)
class MacOSHotkeySpec:
    """Resolved macOS hotkey values."""

    label: str
    key_code: int


class MacOSGlobalHotkeyAdapter:
    """Registers global hotkeys through a macOS backend."""

    _SUPPORTED_KEYS = {"F8": 100}

    def __init__(
        self,
        backend: MacOSHotkeyBackend,
        hotkey_id: int = 1,
    ) -> None:
        self._backend = backend
        self._hotkey_id = hotkey_id
        self._registered: Dict[str, int] = {}

    def register(self, hotkey: str, callback: Callable[[], None]) -> None:
        """Register a supported global hotkey callback."""
        spec = self._parse_hotkey(hotkey)
        if spec.label in self._registered:
            self.unregister(spec.label)
        try:
            self._backend.register(self._hotkey_id, spec.key_code, callback)
        except Exception as exc:
            raise PlatformOperationError(
                "macOS global hotkey could not be registered. "
                "Input Monitoring permission may be required."
            ) from exc
        self._registered[spec.label] = self._hotkey_id

    def unregister(self, hotkey: str) -> None:
        """Unregister a previously registered global hotkey."""
        spec = self._parse_hotkey(hotkey)
        hotkey_id = self._registered.pop(spec.label, None)
        if hotkey_id is None:
            return
        try:
            self._backend.unregister(hotkey_id)
        except Exception as exc:
            raise PlatformOperationError(
                f"macOS global hotkey could not be unregistered: {spec.label}"
            ) from exc

    @classmethod
    def _parse_hotkey(cls, hotkey: str) -> MacOSHotkeySpec:
        normalized = hotkey.strip().upper()
        key_code = cls._SUPPORTED_KEYS.get(normalized)
        if key_code is None:
            raise PlatformOperationError(f"Unsupported macOS hotkey: {hotkey}")
        return MacOSHotkeySpec(label=normalized, key_code=key_code)


class UnavailableMacOSHotkeyBackend:
    """Backend used when macOS hotkey APIs are not available."""

    def register(
        self,
        hotkey_id: int,
        key_code: int,
        callback: Callable[[], None],
    ) -> None:
        raise PlatformOperationError("macOS global hotkey API is not available")

    def unregister(self, hotkey_id: int) -> None:
        raise PlatformOperationError("macOS global hotkey API is not available")


class MacOSQuartzHotkeyApi(Protocol):
    """Minimal Quartz API surface used by the hotkey backend."""

    def is_key_pressed(self, key_code: int) -> bool:
        """Return whether the given macOS virtual key code is currently pressed."""


class MacOSQuartzHotkeyBackend:
    """macOS hotkey backend using global key-state polling."""

    def __init__(
        self,
        api: MacOSQuartzHotkeyApi,
        poll_interval_seconds: float = 0.01,
    ) -> None:
        self._api = api
        self._callbacks: Dict[int, Callable[[], None]] = {}
        self._key_codes: Dict[int, int] = {}
        self._pressed_ids: set[int] = set()
        self._lock = threading.Lock()
        self._listener: Optional[threading.Thread] = None
        self._listener_ready = threading.Event()
        self._poll_interval_seconds = poll_interval_seconds

    def register(
        self,
        hotkey_id: int,
        key_code: int,
        callback: Callable[[], None],
    ) -> None:
        with self._lock:
            self._callbacks[hotkey_id] = callback
            self._key_codes[hotkey_id] = key_code
            self._pressed_ids.discard(hotkey_id)
        self._ensure_listener()

    def unregister(self, hotkey_id: int) -> None:
        with self._lock:
            self._callbacks.pop(hotkey_id, None)
            self._key_codes.pop(hotkey_id, None)
            self._pressed_ids.discard(hotkey_id)

    def dispatch(self, hotkey_id: int) -> None:
        """Dispatch a hotkey callback. Public for backend unit tests."""
        with self._lock:
            callback = self._callbacks.get(hotkey_id)
        if callback is not None:
            try:
                callback()
            except Exception as exc:
                logger.exception(
                    "macOS hotkey callback failed for hotkey_id=%s: %s",
                    hotkey_id,
                    exc,
                )

    def _ensure_listener(self) -> None:
        if self._listener is not None and self._listener.is_alive():
            return
        self._listener = threading.Thread(
            target=self._message_loop,
            name="turkuaz-clickflow-macos-hotkey-listener",
            daemon=True,
        )
        self._listener.start()
        self._listener_ready.wait()

    def _message_loop(self) -> None:
        self._listener_ready.set()
        while True:
            with self._lock:
                tracked_keys = tuple(self._key_codes.items())

            for hotkey_id, key_code in tracked_keys:
                try:
                    is_pressed = self._api.is_key_pressed(key_code)
                except Exception as exc:
                    logger.exception("macOS hotkey state read failed: %s", exc)
                    is_pressed = False

                should_dispatch = False
                with self._lock:
                    was_pressed = hotkey_id in self._pressed_ids
                    if is_pressed and not was_pressed:
                        self._pressed_ids.add(hotkey_id)
                        should_dispatch = hotkey_id in self._callbacks
                    elif not is_pressed and was_pressed:
                        self._pressed_ids.discard(hotkey_id)
                if should_dispatch:
                    self.dispatch(hotkey_id)

            time.sleep(self._poll_interval_seconds)


class MacOSQuartzCtypesHotkeyApi:
    """ctypes wrapper around macOS ApplicationServices key-state APIs."""

    HID_SYSTEM_STATE = 1

    def __init__(self, application_services=None) -> None:
        if application_services is None:
            if sys.platform != "darwin":
                raise PlatformOperationError("macOS global hotkey API is not available")
            application_services = ctypes.cdll.LoadLibrary(
                "/System/Library/Frameworks/ApplicationServices.framework/"
                "ApplicationServices"
            )
        self._api = application_services
        self._configure_signatures()

    def is_key_pressed(self, key_code: int) -> bool:
        return bool(self._api.CGEventSourceKeyState(self.HID_SYSTEM_STATE, key_code))

    def _configure_signatures(self) -> None:
        self._api.CGEventSourceKeyState.argtypes = [ctypes.c_uint32, ctypes.c_uint16]
        self._api.CGEventSourceKeyState.restype = ctypes.c_bool


def create_macos_hotkey_backend() -> MacOSHotkeyBackend:
    """Create the real macOS hotkey backend when available."""
    if sys.platform != "darwin":
        return UnavailableMacOSHotkeyBackend()
    return MacOSQuartzHotkeyBackend(MacOSQuartzCtypesHotkeyApi())
