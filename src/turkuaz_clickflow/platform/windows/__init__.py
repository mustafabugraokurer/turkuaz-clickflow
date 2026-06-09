"""Windows platform adapter shell."""

from dataclasses import dataclass, field

from turkuaz_clickflow.platform.interfaces import PlatformCapabilities
from turkuaz_clickflow.platform.unsupported import (
    UnsupportedWindowQueryAdapter,
)
from turkuaz_clickflow.platform.windows.hotkey import (
    WindowsGlobalHotkeyAdapter,
    create_windows_hotkey_backend,
)
from turkuaz_clickflow.platform.windows.mouse import WindowsMouseClickAdapter
from turkuaz_clickflow.platform.windows.mouse import create_windows_mouse_backend


@dataclass(frozen=True)
class WindowsPlatformAdapter:
    """Windows adapter shell with a mouse adapter boundary."""

    name: str = "windows"
    capabilities: PlatformCapabilities = PlatformCapabilities(
        mouse_click=True,
        global_hotkey=True,
        window_query=False,
    )
    mouse: WindowsMouseClickAdapter = field(
        default_factory=lambda: WindowsMouseClickAdapter(create_windows_mouse_backend())
    )
    hotkeys: WindowsGlobalHotkeyAdapter = field(
        default_factory=lambda: WindowsGlobalHotkeyAdapter(
            create_windows_hotkey_backend()
        )
    )
    windows: UnsupportedWindowQueryAdapter = field(
        default_factory=UnsupportedWindowQueryAdapter
    )
