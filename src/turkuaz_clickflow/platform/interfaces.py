"""Platform adapter contracts.

These protocols define OS-specific capabilities without implementing real
Windows or macOS calls.
"""

from dataclasses import dataclass
from typing import Callable, List, Optional, Protocol


class PlatformOperationError(RuntimeError):
    """Raised by platform adapters when an OS operation fails."""


@dataclass(frozen=True)
class WindowInfo:
    """A user-selectable desktop window."""

    id: str
    title: str
    process_name: Optional[str] = None


@dataclass(frozen=True)
class PlatformCapabilities:
    """Feature support exposed by a platform adapter."""

    mouse_click: bool
    global_hotkey: bool
    window_query: bool


class MouseClickAdapter(Protocol):
    """Contract for OS-specific mouse click implementations."""

    def left_click(self) -> None:
        """Perform one left mouse click."""


class GlobalHotkeyAdapter(Protocol):
    """Contract for OS-specific global hotkey registration."""

    def register(self, hotkey: str, callback: Callable[[], None]) -> None:
        """Register a global hotkey callback."""

    def unregister(self, hotkey: str) -> None:
        """Unregister a global hotkey."""


class WindowQueryAdapter(Protocol):
    """Contract for OS-specific window listing and active window lookup."""

    def list_windows(self) -> List[WindowInfo]:
        """Return selectable windows."""

    def active_window(self) -> Optional[WindowInfo]:
        """Return the currently active window, if available."""


class PlatformAdapter(Protocol):
    """Combined platform adapter used by the app layer."""

    @property
    def name(self) -> str:
        """Human-readable platform name."""

    @property
    def capabilities(self) -> PlatformCapabilities:
        """Supported platform capabilities."""

    @property
    def mouse(self) -> MouseClickAdapter:
        """Mouse click adapter."""

    @property
    def hotkeys(self) -> GlobalHotkeyAdapter:
        """Global hotkey adapter."""

    @property
    def windows(self) -> WindowQueryAdapter:
        """Window query adapter."""

