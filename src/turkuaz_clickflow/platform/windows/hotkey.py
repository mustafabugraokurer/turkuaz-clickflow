"""Windows global hotkey adapter."""

from __future__ import annotations

import sys
import threading
from dataclasses import dataclass
from typing import Callable, Dict, Optional, Protocol

from turkuaz_clickflow.platform.interfaces import PlatformOperationError


class WindowsHotkeyBackend(Protocol):
    """Backend contract for Windows global hotkey registration."""

    def register(
        self,
        hotkey_id: int,
        modifiers: int,
        virtual_key: int,
        callback: Callable[[], None],
    ) -> None:
        """Register a low-level Windows hotkey."""

    def unregister(self, hotkey_id: int) -> None:
        """Unregister a low-level Windows hotkey."""


@dataclass(frozen=True)
class WindowsHotkeySpec:
    """Resolved Windows hotkey values."""

    label: str
    modifiers: int
    virtual_key: int


class WindowsGlobalHotkeyAdapter:
    """Registers global hotkeys through a Windows backend."""

    _SUPPORTED_KEYS = {"F8": 0x77}

    def __init__(
        self,
        backend: WindowsHotkeyBackend,
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
            self._backend.register(
                self._hotkey_id,
                spec.modifiers,
                spec.virtual_key,
                callback,
            )
        except Exception as exc:
            raise PlatformOperationError(
                f"Global hotkey could not be registered: {spec.label}"
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
                f"Global hotkey could not be unregistered: {spec.label}"
            ) from exc

    @classmethod
    def _parse_hotkey(cls, hotkey: str) -> WindowsHotkeySpec:
        normalized = hotkey.strip().upper()
        virtual_key = cls._SUPPORTED_KEYS.get(normalized)
        if virtual_key is None:
            raise PlatformOperationError(f"Unsupported Windows hotkey: {hotkey}")
        return WindowsHotkeySpec(
            label=normalized,
            modifiers=0,
            virtual_key=virtual_key,
        )


class UnavailableWindowsHotkeyBackend:
    """Backend used when Windows APIs are not available in the current process."""

    def register(
        self,
        hotkey_id: int,
        modifiers: int,
        virtual_key: int,
        callback: Callable[[], None],
    ) -> None:
        raise PlatformOperationError("Windows global hotkey API is not available")

    def unregister(self, hotkey_id: int) -> None:
        raise PlatformOperationError("Windows global hotkey API is not available")


class WindowsUser32HotkeyBackend:
    """RegisterHotKey backend with a background message loop."""

    WM_HOTKEY = 0x0312

    def __init__(self, user32: Optional[object] = None) -> None:
        if user32 is None:
            if sys.platform != "win32":
                raise PlatformOperationError(
                    "Windows global hotkey API is not available"
                )
            import ctypes

            user32 = ctypes.windll.user32
        self._user32 = user32
        self._callbacks: Dict[int, Callable[[], None]] = {}
        self._lock = threading.Lock()
        self._listener: Optional[threading.Thread] = None

    def register(
        self,
        hotkey_id: int,
        modifiers: int,
        virtual_key: int,
        callback: Callable[[], None],
    ) -> None:
        if not self._user32.RegisterHotKey(None, hotkey_id, modifiers, virtual_key):
            raise PlatformOperationError("RegisterHotKey failed")
        with self._lock:
            self._callbacks[hotkey_id] = callback
        self._ensure_listener()

    def unregister(self, hotkey_id: int) -> None:
        with self._lock:
            self._callbacks.pop(hotkey_id, None)
        if not self._user32.UnregisterHotKey(None, hotkey_id):
            raise PlatformOperationError("UnregisterHotKey failed")

    def dispatch(self, hotkey_id: int) -> None:
        """Dispatch a hotkey callback. Public for backend unit tests."""
        with self._lock:
            callback = self._callbacks.get(hotkey_id)
        if callback is not None:
            callback()

    def _ensure_listener(self) -> None:
        if self._listener is not None and self._listener.is_alive():
            return
        self._listener = threading.Thread(
            target=self._message_loop,
            name="turkuaz-clickflow-hotkey-listener",
            daemon=True,
        )
        self._listener.start()

    def _message_loop(self) -> None:
        import ctypes
        from ctypes import wintypes

        msg = wintypes.MSG()
        while self._user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
            if msg.message == self.WM_HOTKEY:
                self.dispatch(int(msg.wParam))


def create_windows_hotkey_backend() -> WindowsHotkeyBackend:
    """Create the real Windows backend when available."""
    if sys.platform != "win32":
        return UnavailableWindowsHotkeyBackend()
    return WindowsUser32HotkeyBackend()
