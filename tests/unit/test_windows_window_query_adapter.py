import unittest

from turkuaz_clickflow.platform.interfaces import WindowInfo
from turkuaz_clickflow.platform.windows.window_query import WindowsWindowQueryAdapter


class StubWindowsWindowQueryBackend:
    def __init__(self) -> None:
        self.handles = [101, 202]
        self.active_handle = 202
        self.titles = {
            101: "Untitled - Notepad",
            202: "Calculator",
        }
        self.process_names = {
            101: "notepad.exe",
            202: "calculator.exe",
        }

    def list_window_handles(self):
        return list(self.handles)

    def active_window_handle(self):
        return self.active_handle

    def title_for(self, handle: int) -> str:
        return self.titles.get(handle, "")

    def process_name_for(self, handle: int):
        return self.process_names.get(handle)


class WindowsWindowQueryAdapterTest(unittest.TestCase):
    def test_list_windows_returns_visible_window_info(self) -> None:
        adapter = WindowsWindowQueryAdapter(StubWindowsWindowQueryBackend())

        result = adapter.list_windows()

        self.assertEqual(
            result,
            [
                WindowInfo(
                    id="101",
                    title="Untitled - Notepad",
                    process_name="notepad.exe",
                ),
                WindowInfo(
                    id="202",
                    title="Calculator",
                    process_name="calculator.exe",
                ),
            ],
        )

    def test_list_windows_skips_empty_titles(self) -> None:
        backend = StubWindowsWindowQueryBackend()
        backend.titles[202] = ""
        adapter = WindowsWindowQueryAdapter(backend)

        result = adapter.list_windows()

        self.assertEqual(
            result,
            [
                WindowInfo(
                    id="101",
                    title="Untitled - Notepad",
                    process_name="notepad.exe",
                )
            ],
        )

    def test_active_window_returns_current_window_info(self) -> None:
        adapter = WindowsWindowQueryAdapter(StubWindowsWindowQueryBackend())

        result = adapter.active_window()

        self.assertEqual(
            result,
            WindowInfo(
                id="202",
                title="Calculator",
                process_name="calculator.exe",
            ),
        )

    def test_active_window_returns_none_when_title_is_missing(self) -> None:
        backend = StubWindowsWindowQueryBackend()
        backend.active_handle = 303
        adapter = WindowsWindowQueryAdapter(backend)

        self.assertIsNone(adapter.active_window())


if __name__ == "__main__":
    unittest.main()
