import unittest

from turkuaz_clickflow.platform.interfaces import PlatformOperationError
from turkuaz_clickflow.platform.registry import create_platform_adapter
from turkuaz_clickflow.platform.windows import WindowsPlatformAdapter
from turkuaz_clickflow.platform.windows.hotkey import WindowsGlobalHotkeyAdapter


class FakeWindowsHotkeyBackend:
    def __init__(self) -> None:
        self.registered = []
        self.unregistered = []
        self.callback = None

    def register(self, hotkey_id: int, modifiers: int, virtual_key: int, callback) -> None:
        self.registered.append((hotkey_id, modifiers, virtual_key))
        self.callback = callback

    def unregister(self, hotkey_id: int) -> None:
        self.unregistered.append(hotkey_id)


class FailingWindowsHotkeyBackend:
    def register(self, hotkey_id: int, modifiers: int, virtual_key: int, callback) -> None:
        raise RuntimeError("RegisterHotKey failed")

    def unregister(self, hotkey_id: int) -> None:
        raise RuntimeError("UnregisterHotKey failed")


class WindowsHotkeyAdapterTest(unittest.TestCase):
    def test_windows_hotkey_adapter_registers_f8_virtual_key(self) -> None:
        backend = FakeWindowsHotkeyBackend()
        adapter = WindowsGlobalHotkeyAdapter(backend)
        calls = []

        adapter.register("F8", lambda: calls.append("triggered"))
        backend.callback()

        self.assertEqual(backend.registered, [(1, 0, 0x77)])
        self.assertEqual(calls, ["triggered"])

    def test_windows_hotkey_adapter_unregisters_registered_hotkey(self) -> None:
        backend = FakeWindowsHotkeyBackend()
        adapter = WindowsGlobalHotkeyAdapter(backend)
        adapter.register("F8", lambda: None)

        adapter.unregister("F8")

        self.assertEqual(backend.unregistered, [1])

    def test_windows_hotkey_adapter_rejects_unsupported_hotkey(self) -> None:
        adapter = WindowsGlobalHotkeyAdapter(FakeWindowsHotkeyBackend())

        with self.assertRaises(PlatformOperationError):
            adapter.register("F7", lambda: None)

    def test_windows_hotkey_adapter_wraps_backend_register_errors(self) -> None:
        adapter = WindowsGlobalHotkeyAdapter(FailingWindowsHotkeyBackend())

        with self.assertRaises(PlatformOperationError):
            adapter.register("F8", lambda: None)

    def test_windows_platform_adapter_exposes_global_hotkey_capability(self) -> None:
        adapter = WindowsPlatformAdapter(
            hotkeys=WindowsGlobalHotkeyAdapter(FakeWindowsHotkeyBackend())
        )

        self.assertTrue(adapter.capabilities.global_hotkey)

    def test_registry_windows_adapter_has_global_hotkey_capability(self) -> None:
        adapter = create_platform_adapter("win32")

        self.assertTrue(adapter.capabilities.global_hotkey)


if __name__ == "__main__":
    unittest.main()
