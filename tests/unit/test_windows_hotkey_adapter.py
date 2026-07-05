import unittest
from threading import current_thread

from turkuaz_clickflow.platform.interfaces import PlatformOperationError
from turkuaz_clickflow.platform.registry import create_platform_adapter
from turkuaz_clickflow.platform.windows import WindowsPlatformAdapter
from turkuaz_clickflow.platform.windows.hotkey import (
    WindowsGlobalHotkeyAdapter,
    WindowsUser32HotkeyBackend,
)


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


class FakeUser32PollingBackend:
    def __init__(self) -> None:
        self.key_states = {}

    def GetAsyncKeyState(self, virtual_key: int) -> int:
        return 0x8000 if self.key_states.get(virtual_key, False) else 0

    def set_pressed(self, virtual_key: int, pressed: bool) -> None:
        self.key_states[virtual_key] = pressed


class WindowsHotkeyAdapterTest(unittest.TestCase):
    def test_windows_hotkey_adapter_registers_f8_virtual_key(self) -> None:
        backend = FakeWindowsHotkeyBackend()
        adapter = WindowsGlobalHotkeyAdapter(backend)
        calls = []

        adapter.register("F8", lambda: calls.append("triggered"))
        backend.callback()

        self.assertEqual(backend.registered, [(1, 0x4000, 0x77)])
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

    def test_user32_backend_registers_and_dispatches_on_listener_thread(self) -> None:
        backend = FakeUser32PollingBackend()
        hotkey_backend = WindowsUser32HotkeyBackend(user32=backend, poll_interval_seconds=0.001)
        callbacks = []

        hotkey_backend.register(
            1,
            0x4000,
            0x77,
            lambda: callbacks.append(current_thread().name),
        )
        backend.set_pressed(0x77, True)

        for _ in range(50):
            if callbacks:
                break
            import time

            time.sleep(0.01)

        self.assertTrue(callbacks)
        self.assertEqual(callbacks[0], "turkuaz-clickflow-hotkey-listener")

    def test_user32_backend_unregister_stops_future_dispatch(self) -> None:
        backend = FakeUser32PollingBackend()
        hotkey_backend = WindowsUser32HotkeyBackend(user32=backend, poll_interval_seconds=0.001)
        calls = []

        hotkey_backend.register(1, 0x4000, 0x77, lambda: calls.append("called"))
        hotkey_backend.unregister(1)
        backend.set_pressed(0x77, True)

        import time

        time.sleep(0.02)

        self.assertEqual(calls, [])

    def test_user32_backend_survives_callback_exception_and_dispatches_again(self) -> None:
        backend = FakeUser32PollingBackend()
        hotkey_backend = WindowsUser32HotkeyBackend(user32=backend, poll_interval_seconds=0.001)
        calls = []

        def flaky_callback() -> None:
            calls.append("called")
            if len(calls) == 1:
                raise RuntimeError("boom")

        hotkey_backend.register(1, 0x4000, 0x77, flaky_callback)
        backend.set_pressed(0x77, True)
        import time
        time.sleep(0.02)
        backend.set_pressed(0x77, False)
        time.sleep(0.02)
        backend.set_pressed(0x77, True)

        for _ in range(50):
            if len(calls) >= 2:
                break

            time.sleep(0.01)

        self.assertEqual(calls, ["called", "called"])

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
