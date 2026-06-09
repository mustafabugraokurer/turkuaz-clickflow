"""macOS platform adapter placeholder."""

from dataclasses import dataclass

from turkuaz_clickflow.platform.interfaces import PlatformCapabilities
from turkuaz_clickflow.platform.unsupported import (
    UnsupportedGlobalHotkeyAdapter,
    UnsupportedMouseClickAdapter,
    UnsupportedWindowQueryAdapter,
)


@dataclass(frozen=True)
class MacOSPlatformAdapter:
    """macOS adapter shell. Real OS calls are implemented in later tasks."""

    name: str = "macos"
    capabilities: PlatformCapabilities = PlatformCapabilities(
        mouse_click=False,
        global_hotkey=False,
        window_query=False,
    )
    mouse: UnsupportedMouseClickAdapter = UnsupportedMouseClickAdapter()
    hotkeys: UnsupportedGlobalHotkeyAdapter = UnsupportedGlobalHotkeyAdapter()
    windows: UnsupportedWindowQueryAdapter = UnsupportedWindowQueryAdapter()

