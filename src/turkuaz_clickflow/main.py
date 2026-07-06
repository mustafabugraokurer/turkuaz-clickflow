"""Application entry point for Turkuaz ClickFlow."""

import sys
from typing import List, Optional

from turkuaz_clickflow.app.automation_service import AutomationService
from turkuaz_clickflow.app.click_loop_controller import ClickLoopController
from turkuaz_clickflow.app.click_runner import ClickRunner
from turkuaz_clickflow.app.feedback_service import FeedbackService
from turkuaz_clickflow.app.global_hotkey_controller import GlobalHotkeyController
from turkuaz_clickflow.app.hotkey_service import HotkeyService
from turkuaz_clickflow.config.settings_repository import create_settings_repository
from turkuaz_clickflow.platform.registry import create_platform_adapter
from turkuaz_clickflow.ui.viewmodels.main_window_viewmodel import MainWindowViewModel


def main(argv: Optional[List[str]] = None) -> int:
    """Start the PySide6 MVP main window."""
    from PySide6.QtCore import QObject, Signal
    from PySide6.QtWidgets import QApplication

    from turkuaz_clickflow.ui.views.main_window import (
        MainWindow,
        QTimerClickLoopScheduler,
    )

    app = QApplication(sys.argv if argv is None else argv)

    class HotkeyResultBridge(QObject):
        triggered = Signal(object)

    platform_adapter = create_platform_adapter()
    settings_repository = create_settings_repository()
    automation_service = AutomationService(settings=settings_repository.load())
    feedback_service = FeedbackService()
    hotkey_service = HotkeyService(automation_service)
    view_model = MainWindowViewModel(
        automation_service=automation_service,
        feedback_service=feedback_service,
        hotkey_service=hotkey_service,
        window_query=platform_adapter.windows,
        settings_repository=settings_repository,
    )
    window_holder = {}
    click_runner = ClickRunner(
        automation_service=automation_service,
        mouse=platform_adapter.mouse,
    )
    click_loop_controller = ClickLoopController(
        automation_service=automation_service,
        click_runner=click_runner,
        scheduler=QTimerClickLoopScheduler(),
        feedback_service=feedback_service,
        on_feedback=view_model.show_feedback,
        on_update=lambda: window_holder["window"].refresh(),
        window_query=platform_adapter.windows,
    )
    hotkey_bridge = HotkeyResultBridge()

    def handle_hotkey_trigger(result) -> None:
        view_model.show_hotkey_result(result)
        click_loop_controller.sync_with_automation()
        window_holder["window"].refresh()

    hotkey_bridge.triggered.connect(handle_hotkey_trigger)

    hotkey_controller = GlobalHotkeyController(
        adapter=platform_adapter.hotkeys,
        hotkey_service=hotkey_service,
        feedback_service=feedback_service,
        on_trigger=hotkey_bridge.triggered.emit,
    )
    window = MainWindow(
        view_model,
        click_loop_controller=click_loop_controller,
    )
    window_holder["window"] = window
    registration = hotkey_controller.register()
    if not registration.accepted:
        view_model.show_feedback(registration.message)
        window.refresh()
    window.hotkey_controller = hotkey_controller
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
