import time
import unittest
from threading import current_thread

from turkuaz_clickflow.platform.interfaces import PlatformOperationError
from turkuaz_clickflow.platform.macos import MacOSPlatformAdapter
from turkuaz_clickflow.platform.macos.hotkey import (
    MacOSGlobalHotkeyAdapter,
    MacOSQuartzHotkeyBackend,
    UnavailableMacOSHotkeyBackend,
)
from turkuaz_clickflow.platform.registry import create_platform_adapter


class FakeMacOSHotkeyBackend:
    def __init__(self) -> None:
        self.registered = []
        self.unregistered = []
        self.callback = None

    def register(self, hotkey_id: int, key_code: int, callback) -> None:
        self.registered.append((hotkey_id, key_code))
        self.callback = callback

    def unregister(self, hotkey_id: int) -> None:
        self.unregistered.append(hotkey_id)


class FailingMacOSHotkeyBackend:
    def register(self, hotkey_id: int, key_code: int, callback) -> None:
        raise RuntimeError("CGEventSourceKeyState failed")

    def unregister(self, hotkey_id: int) -> None:
        raise RuntimeError("unregister failed")


class FakeQuartzHotkeyApi:
    def __init__(self) -> None:
        self.key_states = {}

    def is_key_pressed(self, key_code: int) -> bool:
        return bool(self.key_states.get(key_code, False))

    def set_pressed(self, key_code: int, pressed: bool) -> None:
        self.key_states[key_code] = pressed


class MacOSHotkeyAdapterTest(unittest.TestCase):
    def test_macos_hotkey_adapter_registers_f8_key_code(self) -> None:
        backend = FakeMacOSHotkeyBackend()
        adapter = MacOSGlobalHotkeyAdapter(backend)
        calls = []

        adapter.register("F8", lambda: calls.append("triggered"))
        backend.callback()

        self.assertEqual(backend.registered, [(1, 100)])
        self.assertEqual(calls, ["triggered"])

    def test_macos_hotkey_adapter_unregisters_registered_hotkey(self) -> None:
        backend = FakeMacOSHotkeyBackend()
        adapter = MacOSGlobalHotkeyAdapter(backend)
        adapter.register("F8", lambda: None)

        adapter.unregister("F8")

        self.assertEqual(backend.unregistered, [1])

    def test_macos_hotkey_adapter_rejects_unsupported_hotkey(self) -> None:
        adapter = MacOSGlobalHotkeyAdapter(FakeMacOSHotkeyBackend())

        with self.assertRaises(PlatformOperationError):
            adapter.register("F7", lambda: None)

    def test_macos_hotkey_adapter_wraps_backend_register_errors(self) -> None:
        adapter = MacOSGlobalHotkeyAdapter(FailingMacOSHotkeyBackend())

        with self.assertRaises(PlatformOperationError) as context:
            adapter.register("F8", lambda: None)

        self.assertIn("Input Monitoring", str(context.exception))

    def test_quartz_backend_registers_and_dispatches_on_listener_thread(self) -> None:
        api = FakeQuartzHotkeyApi()
        backend = MacOSQuartzHotkeyBackend(api=api, poll_interval_seconds=0.001)
        callbacks = []

        backend.register(1, 100, lambda: callbacks.append(current_thread().name))
        api.set_pressed(100, True)

        for _ in range(50):
            if callbacks:
                break
            time.sleep(0.01)

        self.assertTrue(callbacks)
        self.assertEqual(callbacks[0], "turkuaz-clickflow-macos-hotkey-listener")

    def test_quartz_backend_unregister_stops_future_dispatch(self) -> None:
        api = FakeQuartzHotkeyApi()
        backend = MacOSQuartzHotkeyBackend(api=api, poll_interval_seconds=0.001)
        calls = []

        backend.register(1, 100, lambda: calls.append("called"))
        backend.unregister(1)
        api.set_pressed(100, True)
        time.sleep(0.02)

        self.assertEqual(calls, [])

    def test_quartz_backend_survives_callback_exception_and_dispatches_again(self) -> None:
        api = FakeQuartzHotkeyApi()
        backend = MacOSQuartzHotkeyBackend(api=api, poll_interval_seconds=0.001)
        calls = []

        def flaky_callback() -> None:
            calls.append("called")
            if len(calls) == 1:
                raise RuntimeError("boom")

        backend.register(1, 100, flaky_callback)
        api.set_pressed(100, True)
        time.sleep(0.02)
        api.set_pressed(100, False)
        time.sleep(0.02)
        api.set_pressed(100, True)

        for _ in range(50):
            if len(calls) >= 2:
                break
            time.sleep(0.01)

        self.assertEqual(calls, ["called", "called"])

    def test_unavailable_macos_hotkey_backend_raises_without_os_call(self) -> None:
        backend = UnavailableMacOSHotkeyBackend()

        with self.assertRaises(PlatformOperationError):
            backend.register(1, 100, lambda: None)

    def test_macos_platform_adapter_exposes_global_hotkey_capability(self) -> None:
        adapter = MacOSPlatformAdapter(
            hotkeys=MacOSGlobalHotkeyAdapter(FakeMacOSHotkeyBackend())
        )

        self.assertTrue(adapter.capabilities.global_hotkey)

    def test_registry_macos_adapter_has_global_hotkey_capability(self) -> None:
        adapter = create_platform_adapter("darwin")

        self.assertTrue(adapter.capabilities.global_hotkey)


if __name__ == "__main__":
    unittest.main()
