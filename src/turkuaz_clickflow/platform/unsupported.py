"""Unsupported platform adapter primitives."""

from typing import Callable, List, Optional

from turkuaz_clickflow.platform.interfaces import (
    GlobalHotkeyAdapter,
    MouseClickAdapter,
    PlatformOperationError,
    WindowInfo,
    WindowQueryAdapter,
)


class UnsupportedMouseClickAdapter(MouseClickAdapter):
    """Mouse adapter placeholder that performs no OS calls."""

    def left_click(self) -> None:
        raise PlatformOperationError("Mouse click is not implemented for this platform")


class UnsupportedGlobalHotkeyAdapter(GlobalHotkeyAdapter):
    """Hotkey adapter placeholder that performs no OS calls."""

    def register(self, hotkey: str, callback: Callable[[], None]) -> None:
        raise PlatformOperationError("Global hotkey is not implemented for this platform")

    def unregister(self, hotkey: str) -> None:
        raise PlatformOperationError("Global hotkey is not implemented for this platform")


class UnsupportedWindowQueryAdapter(WindowQueryAdapter):
    """Window adapter placeholder that performs no OS calls."""

    def list_windows(self) -> List[WindowInfo]:
        return []

    def active_window(self) -> Optional[WindowInfo]:
        return None

