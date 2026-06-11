import unittest

from turkuaz_clickflow.platform.interfaces import PlatformOperationError
from turkuaz_clickflow.platform.macos import MacOSPlatformAdapter
from turkuaz_clickflow.platform.macos.mouse import (
    MacOSMouseClickAdapter,
    MacOSPoint,
    MacOSQuartzMouseBackend,
    UnavailableMacOSMouseBackend,
)
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


class FakeQuartzApi:
    def __init__(self, trusted: bool = True, create_event: bool = True) -> None:
        self.trusted = trusted
        self.create_event = create_event
        self.created_events = []
        self.posted_events = []
        self.released_events = []

    def is_process_trusted(self) -> bool:
        return self.trusted

    def current_mouse_location(self) -> MacOSPoint:
        return MacOSPoint(12.0, 24.0)

    def create_mouse_event(self, event_type: int, point: MacOSPoint, button: int):
        if not self.create_event:
            raise PlatformOperationError("Could not create macOS mouse event")
        event = f"event-{event_type}-{point.x}-{point.y}-{button}"
        self.created_events.append((event_type, point, button))
        return event

    def post_event(self, event) -> None:
        self.posted_events.append(event)

    def release_event(self, event) -> None:
        self.released_events.append(event)


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

    def test_macos_mouse_adapter_delegates_left_click_to_backend(self) -> None:
        backend = FakeMouseBackend()
        adapter = MacOSMouseClickAdapter(backend)

        adapter.left_click()

        self.assertEqual(backend.clicks, 1)

    def test_macos_mouse_adapter_wraps_backend_errors(self) -> None:
        adapter = MacOSMouseClickAdapter(FailingMouseBackend())

        with self.assertRaises(PlatformOperationError):
            adapter.left_click()

    def test_macos_mouse_adapter_preserves_platform_error_message(self) -> None:
        class PermissionMouseBackend:
            def left_click(self) -> None:
                raise PlatformOperationError(
                    "macOS Accessibility or Input Monitoring permission is required"
                )

        adapter = MacOSMouseClickAdapter(PermissionMouseBackend())

        with self.assertRaises(PlatformOperationError) as context:
            adapter.left_click()

        self.assertIn("Accessibility", str(context.exception))

    def test_macos_quartz_backend_posts_left_down_and_up_events(self) -> None:
        api = FakeQuartzApi()
        backend = MacOSQuartzMouseBackend(api)

        backend.left_click()

        self.assertEqual(
            api.created_events,
            [
                (1, MacOSPoint(12.0, 24.0), 0),
                (2, MacOSPoint(12.0, 24.0), 0),
            ],
        )
        self.assertEqual(api.posted_events, ["event-1-12.0-24.0-0", "event-2-12.0-24.0-0"])
        self.assertEqual(api.released_events, ["event-1-12.0-24.0-0", "event-2-12.0-24.0-0"])

    def test_macos_quartz_backend_requires_accessibility_permission(self) -> None:
        backend = MacOSQuartzMouseBackend(FakeQuartzApi(trusted=False))

        with self.assertRaises(PlatformOperationError):
            backend.left_click()

    def test_macos_quartz_backend_releases_created_events_when_post_fails(self) -> None:
        class FailingPostQuartzApi(FakeQuartzApi):
            def post_event(self, event) -> None:
                raise PlatformOperationError("post failed")

        api = FailingPostQuartzApi()
        backend = MacOSQuartzMouseBackend(api)

        with self.assertRaises(PlatformOperationError):
            backend.left_click()

        self.assertEqual(api.released_events, ["event-1-12.0-24.0-0", "event-2-12.0-24.0-0"])

    def test_unavailable_macos_mouse_backend_raises_without_os_call(self) -> None:
        backend = UnavailableMacOSMouseBackend()

        with self.assertRaises(PlatformOperationError):
            backend.left_click()

    def test_macos_platform_adapter_exposes_mouse_click_capability(self) -> None:
        adapter = MacOSPlatformAdapter(
            mouse=MacOSMouseClickAdapter(FakeMouseBackend())
        )

        self.assertTrue(adapter.capabilities.mouse_click)
        adapter.mouse.left_click()

    def test_registry_macos_adapter_has_mouse_click_capability(self) -> None:
        adapter = create_platform_adapter("darwin")

        self.assertTrue(adapter.capabilities.mouse_click)


if __name__ == "__main__":
    unittest.main()
