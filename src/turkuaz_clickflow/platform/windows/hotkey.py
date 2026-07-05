"""Windows global hotkey adapter."""

from __future__ import annotations

import sys
import threading
import time
import logging
from dataclasses import dataclass
from typing import Callable, Dict, Optional, Protocol

from turkuaz_clickflow.platform.interfaces import PlatformOperationError


logger = logging.getLogger(__name__)


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

    _MOD_NOREPEAT = 0x4000
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
            modifiers=cls._MOD_NOREPEAT,
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
    """Windows hotkey backend using global key-state polling."""

    def __init__(
        self,
        user32: Optional[object] = None,
        poll_interval_seconds: float = 0.01,
    ) -> None:
        if user32 is None:
            if sys.platform != "win32":
                raise PlatformOperationError(
                    "Windows global hotkey API is not available"
                )
            import ctypes

            user32 = ctypes.windll.user32
        self._user32 = user32
        self._callbacks: Dict[int, Callable[[], None]] = {}
        self._virtual_keys: Dict[int, int] = {}
        self._pressed_ids: set[int] = set()
        self._lock = threading.Lock()
        self._listener: Optional[threading.Thread] = None
        self._listener_ready = threading.Event()
        self._poll_interval_seconds = poll_interval_seconds

    def register(
        self,
        hotkey_id: int,
        modifiers: int,
        virtual_key: int,
        callback: Callable[[], None],
    ) -> None:
        del modifiers
        with self._lock:
            self._callbacks[hotkey_id] = callback
            self._virtual_keys[hotkey_id] = virtual_key
            self._pressed_ids.discard(hotkey_id)
        self._ensure_listener()

    def unregister(self, hotkey_id: int) -> None:
        with self._lock:
            self._callbacks.pop(hotkey_id, None)
            self._virtual_keys.pop(hotkey_id, None)
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
                    "Windows hotkey callback failed for hotkey_id=%s: %s",
                    hotkey_id,
                    exc,
                )

    def _ensure_listener(self) -> None:
        if self._listener is not None and self._listener.is_alive():
            return
        self._listener = threading.Thread(
            target=self._message_loop,
            name="turkuaz-clickflow-hotkey-listener",
            daemon=True,
        )
        self._listener.start()
        self._listener_ready.wait()

    def _message_loop(self) -> None:
        self._listener_ready.set()
        while True:
            with self._lock:
                tracked_keys = tuple(self._virtual_keys.items())

            for hotkey_id, virtual_key in tracked_keys:
                is_pressed = bool(self._user32.GetAsyncKeyState(int(virtual_key)) & 0x8000)
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


def create_windows_hotkey_backend() -> WindowsHotkeyBackend:
    """Create the real Windows backend when available."""
    if sys.platform != "win32":
        return UnavailableWindowsHotkeyBackend()
    return WindowsUser32HotkeyBackend()
