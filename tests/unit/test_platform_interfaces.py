import unittest

from turkuaz_clickflow.platform.interfaces import (
    PlatformOperationError,
    WindowInfo,
)
from turkuaz_clickflow.platform.registry import create_platform_adapter, platform_key
from turkuaz_clickflow.platform.unsupported import (
    UnsupportedGlobalHotkeyAdapter,
    UnsupportedMouseClickAdapter,
    UnsupportedWindowQueryAdapter,
)


class PlatformInterfacesTest(unittest.TestCase):
    def test_window_info_carries_user_visible_window_data(self) -> None:
        info = WindowInfo(id="42", title="Example", process_name="example.exe")

        self.assertEqual(info.id, "42")
        self.assertEqual(info.title, "Example")
        self.assertEqual(info.process_name, "example.exe")

    def test_platform_key_normalizes_supported_systems(self) -> None:
        self.assertEqual(platform_key("win32"), "windows")
        self.assertEqual(platform_key("darwin"), "macos")
        self.assertEqual(platform_key("linux"), "unsupported")

    def test_create_platform_adapter_returns_windows_shell(self) -> None:
        adapter = create_platform_adapter("win32")

        self.assertEqual(adapter.name, "windows")
        self.assertTrue(adapter.capabilities.mouse_click)
        self.assertTrue(adapter.capabilities.global_hotkey)
        self.assertTrue(adapter.capabilities.window_query)

    def test_create_platform_adapter_returns_macos_shell(self) -> None:
        adapter = create_platform_adapter("darwin")

        self.assertEqual(adapter.name, "macos")
        self.assertTrue(adapter.capabilities.mouse_click)
        self.assertFalse(adapter.capabilities.global_hotkey)
        self.assertFalse(adapter.capabilities.window_query)

    def test_unsupported_platform_raises(self) -> None:
        with self.assertRaises(RuntimeError):
            create_platform_adapter("linux")

    def test_unsupported_mouse_adapter_does_not_call_os(self) -> None:
        with self.assertRaises(PlatformOperationError):
            UnsupportedMouseClickAdapter().left_click()

    def test_unsupported_hotkey_adapter_does_not_call_os(self) -> None:
        adapter = UnsupportedGlobalHotkeyAdapter()

        with self.assertRaises(PlatformOperationError):
            adapter.register("F8", lambda: None)

        with self.assertRaises(PlatformOperationError):
            adapter.unregister("F8")

    def test_unsupported_window_adapter_returns_empty_state(self) -> None:
        adapter = UnsupportedWindowQueryAdapter()

        self.assertEqual(adapter.list_windows(), [])
        self.assertIsNone(adapter.active_window())


if __name__ == "__main__":
    unittest.main()
