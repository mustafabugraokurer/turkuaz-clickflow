import unittest

from turkuaz_clickflow.platform.interfaces import PlatformOperationError
from turkuaz_clickflow.platform.macos import MacOSPlatformAdapter
from turkuaz_clickflow.platform.registry import create_platform_adapter
from turkuaz_clickflow.platform.windows import WindowsPlatformAdapter
from turkuaz_clickflow.platform.windows.mouse import (
    UnavailableWindowsMouseBackend,
    WindowsMouseClickAdapter,
    WindowsUser32MouseBackend,
)


class FakeMouseBackend:
    def __init__(self) -> None:
        self.clicks = 0

    def left_click(self) -> None:
        self.clicks += 1


class FailingMouseBackend:
    def left_click(self) -> None:
        raise RuntimeError("backend failed")


class FakeUser32:
    def __init__(self, send_input_result: int = 2) -> None:
        self.send_input_result = send_input_result
        self.calls = []

    def SendInput(self, count, inputs, input_size):
        self.calls.append((count, input_size))
        return self.send_input_result


class MouseClickAdapterTest(unittest.TestCase):
    def test_windows_mouse_adapter_delegates_left_click_to_backend(self) -> None:
        backend = FakeMouseBackend()
        adapter = WindowsMouseClickAdapter(backend)

        adapter.left_click()

        self.assertEqual(backend.clicks, 1)

    def test_windows_mouse_adapter_wraps_backend_errors(self) -> None:
        adapter = WindowsMouseClickAdapter(FailingMouseBackend())

        with self.assertRaises(PlatformOperationError):
            adapter.left_click()

    def test_windows_user32_backend_sends_left_down_and_up_inputs(self) -> None:
        user32 = FakeUser32()
        backend = WindowsUser32MouseBackend(user32=user32)

        backend.left_click()

        self.assertEqual(len(user32.calls), 1)
        self.assertEqual(user32.calls[0][0], 2)

    def test_windows_user32_backend_raises_when_send_input_fails(self) -> None:
        backend = WindowsUser32MouseBackend(user32=FakeUser32(send_input_result=1))

        with self.assertRaises(PlatformOperationError):
            backend.left_click()

    def test_unavailable_windows_mouse_backend_raises_without_os_call(self) -> None:
        backend = UnavailableWindowsMouseBackend()

        with self.assertRaises(PlatformOperationError):
            backend.left_click()

    def test_windows_platform_adapter_exposes_mouse_click_capability(self) -> None:
        adapter = WindowsPlatformAdapter(mouse=WindowsMouseClickAdapter(FakeMouseBackend()))

        self.assertTrue(adapter.capabilities.mouse_click)
        adapter.mouse.left_click()

    def test_registry_windows_adapter_has_mouse_click_capability(self) -> None:
        adapter = create_platform_adapter("win32")

        self.assertTrue(adapter.capabilities.mouse_click)

    def test_macos_platform_adapter_keeps_mouse_click_as_placeholder(self) -> None:
        adapter = MacOSPlatformAdapter()

        self.assertFalse(adapter.capabilities.mouse_click)
        with self.assertRaises(PlatformOperationError):
            adapter.mouse.left_click()


if __name__ == "__main__":
    unittest.main()
