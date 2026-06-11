"""macOS platform adapter."""

from dataclasses import dataclass, field

from turkuaz_clickflow.platform.interfaces import PlatformCapabilities
from turkuaz_clickflow.platform.unsupported import (
    UnsupportedGlobalHotkeyAdapter,
    UnsupportedWindowQueryAdapter,
)
from turkuaz_clickflow.platform.macos.mouse import (
    MacOSMouseClickAdapter,
    create_macos_mouse_backend,
)


@dataclass(frozen=True)
class MacOSPlatformAdapter:
    """macOS adapter shell with a mouse adapter boundary."""

    name: str = "macos"
    capabilities: PlatformCapabilities = PlatformCapabilities(
        mouse_click=True,
        global_hotkey=False,
        window_query=False,
    )
    mouse: MacOSMouseClickAdapter = field(
        default_factory=lambda: MacOSMouseClickAdapter(create_macos_mouse_backend())
    )
    hotkeys: UnsupportedGlobalHotkeyAdapter = UnsupportedGlobalHotkeyAdapter()
    windows: UnsupportedWindowQueryAdapter = UnsupportedWindowQueryAdapter()
