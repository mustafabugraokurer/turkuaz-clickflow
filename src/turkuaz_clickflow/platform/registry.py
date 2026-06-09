"""Platform adapter selection."""

import sys

from turkuaz_clickflow.platform.interfaces import PlatformAdapter
from turkuaz_clickflow.platform.macos import MacOSPlatformAdapter
from turkuaz_clickflow.platform.windows import WindowsPlatformAdapter


def platform_key(system_platform: str = sys.platform) -> str:
    """Return the normalized platform key for adapter selection."""
    if system_platform.startswith("win"):
        return "windows"
    if system_platform == "darwin":
        return "macos"
    return "unsupported"


def create_platform_adapter(system_platform: str = sys.platform) -> PlatformAdapter:
    """Create the platform adapter shell for the current OS."""
    key = platform_key(system_platform)
    if key == "windows":
        return WindowsPlatformAdapter()
    if key == "macos":
        return MacOSPlatformAdapter()
    raise RuntimeError(f"Unsupported platform: {system_platform}")

