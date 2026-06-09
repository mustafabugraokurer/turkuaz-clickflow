"""Windows mouse click adapter."""

from __future__ import annotations

import sys
from typing import Protocol

from turkuaz_clickflow.platform.interfaces import PlatformOperationError


class WindowsMouseBackend(Protocol):
    """Backend contract for one low-level Windows left click."""

    def left_click(self) -> None:
        """Perform the low-level left click operation."""


class WindowsMouseClickAdapter:
    """Mouse click adapter for Windows.

    The concrete OS backend is injected so tests do not perform real clicks.
    """

    def __init__(self, backend: WindowsMouseBackend) -> None:
        self._backend = backend

    def left_click(self) -> None:
        """Perform one left click through the configured backend."""
        try:
            self._backend.left_click()
        except Exception as exc:
            raise PlatformOperationError("Windows left click failed") from exc


class UnavailableWindowsMouseBackend:
    """Backend used when Windows mouse APIs are not available."""

    def left_click(self) -> None:
        raise PlatformOperationError("Windows mouse API is not available")


class WindowsUser32MouseBackend:
    """Real Windows backend using SendInput for one left click."""

    def __init__(self, user32: object | None = None) -> None:
        if user32 is None:
            if sys.platform != "win32":
                raise PlatformOperationError("Windows mouse API is not available")
            import ctypes

            user32 = ctypes.windll.user32
        self._user32 = user32

    def left_click(self) -> None:
        import ctypes
        from ctypes import wintypes

        class MOUSEINPUT(ctypes.Structure):
            _fields_ = [
                ("dx", wintypes.LONG),
                ("dy", wintypes.LONG),
                ("mouseData", wintypes.DWORD),
                ("dwFlags", wintypes.DWORD),
                ("time", wintypes.DWORD),
                ("dwExtraInfo", ctypes.POINTER(wintypes.ULONG)),
            ]

        class INPUTUNION(ctypes.Union):
            _fields_ = [("mi", MOUSEINPUT)]

        class INPUT(ctypes.Structure):
            _fields_ = [
                ("type", wintypes.DWORD),
                ("union", INPUTUNION),
            ]

        input_mouse = 0
        left_down = 0x0002
        left_up = 0x0004
        inputs = (INPUT * 2)(
            INPUT(
                type=input_mouse,
                union=INPUTUNION(
                    mi=MOUSEINPUT(0, 0, 0, left_down, 0, None)
                ),
            ),
            INPUT(
                type=input_mouse,
                union=INPUTUNION(
                    mi=MOUSEINPUT(0, 0, 0, left_up, 0, None)
                ),
            ),
        )

        sent = self._user32.SendInput(2, ctypes.byref(inputs), ctypes.sizeof(INPUT))
        if sent != 2:
            raise PlatformOperationError("Windows SendInput left click failed")


def create_windows_mouse_backend() -> WindowsMouseBackend:
    """Create the real Windows mouse backend when available."""
    if sys.platform != "win32":
        return UnavailableWindowsMouseBackend()
    return WindowsUser32MouseBackend()
