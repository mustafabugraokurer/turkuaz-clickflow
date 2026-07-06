import unittest

from turkuaz_clickflow.app.automation_service import AutomationService
from turkuaz_clickflow.app.feedback_service import FeedbackService
from turkuaz_clickflow.domain.automation_state import AutomationState
from turkuaz_clickflow.domain.stop_reason import StopReason
from turkuaz_clickflow.platform.interfaces import WindowInfo
from turkuaz_clickflow.ui.viewmodels.main_window_viewmodel import MainWindowViewModel


class StubWindowQueryAdapter:
    def __init__(self, windows=None) -> None:
        self._windows = list(windows or [])

    def list_windows(self):
        return list(self._windows)

    def active_window(self):
        return self._windows[0] if self._windows else None

    def set_windows(self, windows) -> None:
        self._windows = list(windows)


class FakeSettingsRepository:
    def __init__(self) -> None:
        self.saved = []

    def load(self):
        raise AssertionError("viewmodel should not load settings")

    def save(self, settings) -> None:
        self.saved.append(settings)


class MainWindowViewModelTest(unittest.TestCase):
    def test_default_snapshot_matches_mvp_wireframe_values(self) -> None:
        view_model = MainWindowViewModel(
            automation_service=AutomationService(),
            feedback_service=FeedbackService(),
        )

        snapshot = view_model.snapshot()

        self.assertEqual(snapshot.title, "Turkuaz ClickFlow")
        self.assertEqual(snapshot.status, "ready")
        self.assertEqual(snapshot.cps, 10)
        self.assertEqual(snapshot.hotkey, "F8")
        self.assertEqual(snapshot.click_count, 0)
        self.assertEqual(snapshot.elapsed_time, "00:00:00")
        self.assertEqual(snapshot.available_target_windows, ())
        self.assertEqual(snapshot.target_window, "Seçilmedi")
        self.assertFalse(snapshot.window_guard_enabled)
        self.assertEqual(
            snapshot.message,
            "Hazır. Başlatmak için Start'a basın veya F8 kullanın.",
        )
        self.assertEqual(snapshot.message_level, "info")
        self.assertTrue(snapshot.start_enabled)
        self.assertFalse(snapshot.stop_enabled)

    def test_snapshot_exposes_available_target_windows(self) -> None:
        adapter = StubWindowQueryAdapter(
            [
                WindowInfo(id="1", title="Untitled - Notepad"),
                WindowInfo(id="2", title="Calculator"),
            ]
        )
        view_model = MainWindowViewModel(
            automation_service=AutomationService(),
            feedback_service=FeedbackService(),
            window_query=adapter,
        )

        snapshot = view_model.snapshot()

        self.assertEqual(
            snapshot.available_target_windows,
            (
                WindowInfo(id="1", title="Untitled - Notepad"),
                WindowInfo(id="2", title="Calculator"),
            ),
        )

    def test_select_target_window_updates_next_run_selection(self) -> None:
        adapter = StubWindowQueryAdapter([WindowInfo(id="1", title="Untitled - Notepad")])
        view_model = MainWindowViewModel(
            automation_service=AutomationService(),
            feedback_service=FeedbackService(),
            window_query=adapter,
        )

        snapshot = view_model.select_target_window("1")

        self.assertEqual(snapshot.target_window, "Untitled - Notepad")

    def test_missing_selected_target_window_falls_back_to_unselected(self) -> None:
        adapter = StubWindowQueryAdapter([WindowInfo(id="1", title="Untitled - Notepad")])
        view_model = MainWindowViewModel(
            automation_service=AutomationService(),
            feedback_service=FeedbackService(),
            window_query=adapter,
        )
        view_model.select_target_window("1")
        adapter.set_windows([])

        snapshot = view_model.snapshot()

        self.assertEqual(snapshot.target_window, "Seçilmedi")

    def test_start_command_uses_automation_service(self) -> None:
        automation = AutomationService()
        view_model = MainWindowViewModel(
            automation_service=automation,
            feedback_service=FeedbackService(),
        )

        snapshot = view_model.start(cps=12)

        self.assertEqual(automation.state, AutomationState.RUNNING)
        self.assertEqual(automation.settings.cps, 12)
        self.assertEqual(snapshot.status, "running")
        self.assertFalse(snapshot.start_enabled)
        self.assertTrue(snapshot.stop_enabled)
        self.assertEqual(
            snapshot.message,
            "Çalışıyor. Durdurmak için Stop'a basın veya F8 kullanın.",
        )

    def test_start_carries_selected_target_window_into_settings(self) -> None:
        automation = AutomationService()
        adapter = StubWindowQueryAdapter([WindowInfo(id="1", title="Untitled - Notepad")])
        view_model = MainWindowViewModel(
            automation_service=automation,
            feedback_service=FeedbackService(),
            window_query=adapter,
        )
        view_model.select_target_window("1")
        view_model.set_window_guard_enabled(True)

        view_model.start(cps=12)

        self.assertEqual(automation.settings.target_window_id, "1")
        self.assertEqual(automation.settings.target_window, "Untitled - Notepad")
        self.assertTrue(automation.settings.window_guard_enabled)

    def test_target_window_and_guard_selection_are_saved(self) -> None:
        repository = FakeSettingsRepository()
        adapter = StubWindowQueryAdapter([WindowInfo(id="1", title="Untitled - Notepad")])
        view_model = MainWindowViewModel(
            automation_service=AutomationService(),
            feedback_service=FeedbackService(),
            window_query=adapter,
            settings_repository=repository,
        )

        view_model.select_target_window("1")
        view_model.set_window_guard_enabled(True)

        self.assertEqual(repository.saved[-1].target_window_id, "1")
        self.assertEqual(repository.saved[-1].target_window, "Untitled - Notepad")
        self.assertTrue(repository.saved[-1].window_guard_enabled)

    def test_cps_selection_is_preserved_before_start(self) -> None:
        view_model = MainWindowViewModel(
            automation_service=AutomationService(),
            feedback_service=FeedbackService(),
        )

        changed = view_model.set_cps(25)
        refreshed = view_model.snapshot()

        self.assertEqual(changed.cps, 25)
        self.assertEqual(refreshed.cps, 25)
        self.assertEqual(view_model.selected_cps, 25)

    def test_cps_selection_is_saved_when_repository_is_configured(self) -> None:
        repository = FakeSettingsRepository()
        view_model = MainWindowViewModel(
            automation_service=AutomationService(),
            feedback_service=FeedbackService(),
            settings_repository=repository,
        )

        view_model.set_cps(25)

        self.assertEqual(repository.saved[-1].cps, 25)

    def test_start_uses_and_preserves_selected_cps(self) -> None:
        automation = AutomationService()
        view_model = MainWindowViewModel(
            automation_service=automation,
            feedback_service=FeedbackService(),
        )
        view_model.set_cps(25)

        snapshot = view_model.start(cps=view_model.selected_cps)

        self.assertEqual(automation.settings.cps, 25)
        self.assertEqual(snapshot.cps, 25)
        self.assertEqual(view_model.snapshot().cps, 25)

    def test_stop_command_uses_automation_service(self) -> None:
        automation = AutomationService()
        view_model = MainWindowViewModel(
            automation_service=automation,
            feedback_service=FeedbackService(),
        )
        view_model.start(cps=10)

        snapshot = view_model.stop()

        self.assertEqual(automation.state, AutomationState.STOPPED)
        self.assertEqual(automation.stop_reason, StopReason.USER_STOPPED)
        self.assertEqual(snapshot.status, "stopped")
        self.assertTrue(snapshot.start_enabled)
        self.assertFalse(snapshot.stop_enabled)
        self.assertEqual(
            snapshot.message,
            "Durdu. Son durma sebebi: Kullanıcı durdurdu.",
        )

    def test_stop_preserves_selected_cps_for_next_run(self) -> None:
        automation = AutomationService()
        view_model = MainWindowViewModel(
            automation_service=automation,
            feedback_service=FeedbackService(),
        )
        view_model.set_cps(30)
        view_model.start(cps=view_model.selected_cps)

        snapshot = view_model.stop()

        self.assertEqual(snapshot.cps, 30)
        self.assertEqual(view_model.snapshot().cps, 30)

    def test_invalid_cps_start_returns_user_message(self) -> None:
        automation = AutomationService()
        view_model = MainWindowViewModel(
            automation_service=automation,
            feedback_service=FeedbackService(),
        )

        snapshot = view_model.start(cps=101)

        self.assertEqual(automation.state, AutomationState.ERROR)
        self.assertEqual(automation.stop_reason, StopReason.INVALID_SETTINGS)
        self.assertEqual(snapshot.status, "error")
        self.assertFalse(snapshot.start_enabled)
        self.assertFalse(snapshot.stop_enabled)
        self.assertEqual(snapshot.message_level, "warning")
        self.assertEqual(snapshot.message, "CPS değeri 1 ile 100 arasında olmalıdır.")

    def test_snapshot_reflects_counter_and_elapsed_values(self) -> None:
        automation = AutomationService()
        view_model = MainWindowViewModel(
            automation_service=automation,
            feedback_service=FeedbackService(),
        )
        view_model.start(cps=10)

        automation.record_successful_click(2)
        snapshot = view_model.snapshot()

        self.assertEqual(snapshot.click_count, 2)
        self.assertEqual(snapshot.elapsed_time, "00:00:00")

    def test_hotkey_trigger_routes_through_hotkey_service(self) -> None:
        automation = AutomationService()
        view_model = MainWindowViewModel(
            automation_service=automation,
            feedback_service=FeedbackService(),
        )

        first = view_model.trigger_hotkey("F8")
        second = view_model.trigger_hotkey("F8")

        self.assertEqual(first.status, "running")
        self.assertEqual(second.status, "stopped")
        self.assertEqual(automation.stop_reason, StopReason.HOTKEY_STOPPED)
        self.assertEqual(
            second.message,
            "Durdu. Son durma sebebi: F8 ile durduruldu.",
        )

    def test_elapsed_time_is_formatted_for_display(self) -> None:
        self.assertEqual(MainWindowViewModel._format_elapsed(0), "00:00:00")
        self.assertEqual(MainWindowViewModel._format_elapsed(65), "00:01:05")
        self.assertEqual(MainWindowViewModel._format_elapsed(3661), "01:01:01")


if __name__ == "__main__":
    unittest.main()
