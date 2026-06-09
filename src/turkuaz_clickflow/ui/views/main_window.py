"""PySide6 MVP main window."""

from typing import Callable, Optional

from turkuaz_clickflow.app.click_loop_controller import ClickLoopController
from turkuaz_clickflow.ui.viewmodels.main_window_viewmodel import (
    MainWindowSnapshot,
    MainWindowViewModel,
)

try:
    from PySide6.QtCore import QTimer, Qt
    from PySide6.QtWidgets import (
        QCheckBox,
        QComboBox,
        QFormLayout,
        QFrame,
        QGridLayout,
        QGroupBox,
        QHBoxLayout,
        QLabel,
        QMainWindow,
        QPushButton,
        QSpinBox,
        QVBoxLayout,
        QWidget,
    )
except ImportError as exc:  # pragma: no cover - exercised only without PySide6.
    raise ImportError("PySide6 is required to use MainWindow") from exc


class MainWindow(QMainWindow):
    """Main application window matching the Sprint-1 wireframe."""

    def __init__(
        self,
        view_model: MainWindowViewModel,
        click_loop_controller: Optional[ClickLoopController] = None,
    ) -> None:
        super().__init__()
        self._view_model = view_model
        self._click_loop_controller = click_loop_controller

        self.setWindowTitle("Turkuaz ClickFlow")
        self.setMinimumSize(560, 420)

        self.title_label = QLabel("Turkuaz ClickFlow")
        self.title_label.setObjectName("titleLabel")
        self.status_label = QLabel()
        self.status_label.setObjectName("statusLabel")

        self.start_button = QPushButton("Start")
        self.start_button.setObjectName("startButton")
        self.stop_button = QPushButton("Stop")
        self.stop_button.setObjectName("stopButton")
        self.hotkey_label = QLabel()
        self.hotkey_label.setObjectName("hotkeyLabel")

        self.cps_input = QSpinBox()
        self.cps_input.setObjectName("cpsInput")
        self.cps_input.setRange(1, 100)
        self.cps_range_label = QLabel("Min: 1     Max: 100")

        self.target_window_select = QComboBox()
        self.target_window_select.setObjectName("targetWindowSelect")
        self.target_window_select.addItem("Seçilmedi")
        self.window_guard_checkbox = QCheckBox("Pencere değişince durdur")
        self.window_guard_checkbox.setObjectName("windowGuardCheckbox")

        self.click_count_label = QLabel()
        self.click_count_label.setObjectName("clickCountLabel")
        self.elapsed_time_label = QLabel()
        self.elapsed_time_label.setObjectName("elapsedTimeLabel")

        self.message_label = QLabel()
        self.message_label.setObjectName("messageLabel")
        self.message_label.setWordWrap(True)

        self.setCentralWidget(self._build_content())
        self._connect_signals()
        self._refresh_timer = QTimer(self)
        self._refresh_timer.setInterval(1000)
        self._refresh_timer.timeout.connect(self.refresh)
        self._refresh_timer.start()
        self.refresh()

    def refresh(self) -> None:
        """Refresh display values from the view model."""
        self._apply_snapshot(self._view_model.snapshot())

    def _connect_signals(self) -> None:
        self.start_button.clicked.connect(self._handle_start)
        self.stop_button.clicked.connect(self._handle_stop)

    def _handle_start(self) -> None:
        self._apply_snapshot(self._view_model.start(cps=self.cps_input.value()))
        self._sync_click_loop()

    def _handle_stop(self) -> None:
        self._apply_snapshot(self._view_model.stop())
        self._sync_click_loop()

    def sync_after_external_automation_change(self) -> None:
        """Refresh UI and click loop after OS hotkey callbacks."""
        self._sync_click_loop()
        self.refresh()

    def _build_content(self) -> QWidget:
        root = QWidget()
        layout = QVBoxLayout(root)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(12)

        header = QHBoxLayout()
        header.addWidget(self.title_label)
        header.addStretch(1)
        header.addWidget(self.status_label)
        layout.addLayout(header)

        layout.addWidget(self._divider())
        layout.addWidget(self._build_control_group())
        layout.addWidget(self._build_speed_group())
        layout.addWidget(self._build_window_group())
        layout.addWidget(self._build_stats_group())
        layout.addWidget(self._build_message_group())
        layout.addStretch(1)
        return root

    def _build_control_group(self) -> QGroupBox:
        group = QGroupBox("Kontrol")
        layout = QHBoxLayout(group)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        layout.addSpacing(12)
        layout.addWidget(self.hotkey_label)
        layout.addStretch(1)
        return group

    def _build_speed_group(self) -> QGroupBox:
        group = QGroupBox("Hız Ayarı")
        layout = QHBoxLayout(group)
        layout.addWidget(QLabel("CPS:"))
        layout.addWidget(self.cps_input)
        layout.addSpacing(12)
        layout.addWidget(self.cps_range_label)
        layout.addStretch(1)
        return group

    def _build_window_group(self) -> QGroupBox:
        group = QGroupBox("Pencere")
        layout = QFormLayout(group)
        layout.addRow("Hedef pencere:", self.target_window_select)
        layout.addRow("", self.window_guard_checkbox)
        return group

    def _build_stats_group(self) -> QGroupBox:
        group = QGroupBox("Çalışma Bilgisi")
        layout = QGridLayout(group)
        layout.addWidget(QLabel("Tıklama sayısı:"), 0, 0)
        layout.addWidget(self.click_count_label, 0, 1)
        layout.addWidget(QLabel("Çalışma süresi:"), 1, 0)
        layout.addWidget(self.elapsed_time_label, 1, 1)
        layout.setColumnStretch(2, 1)
        return group

    def _build_message_group(self) -> QGroupBox:
        group = QGroupBox("Mesaj")
        layout = QVBoxLayout(group)
        layout.addWidget(self.message_label)
        return group

    def _divider(self) -> QFrame:
        divider = QFrame()
        divider.setFrameShape(QFrame.HLine)
        divider.setFrameShadow(QFrame.Sunken)
        return divider

    def _apply_snapshot(self, snapshot: MainWindowSnapshot) -> None:
        self.title_label.setText(snapshot.title)
        self.status_label.setText(f"Durum: {self._localize_status(snapshot.status)}")
        self.hotkey_label.setText(f"Kısayol: {snapshot.hotkey}")
        self.cps_input.setValue(snapshot.cps)
        self._sync_target_window(snapshot.target_window)
        self.window_guard_checkbox.setChecked(snapshot.window_guard_enabled)
        self.click_count_label.setText(str(snapshot.click_count))
        self.elapsed_time_label.setText(snapshot.elapsed_time)
        self.message_label.setText(snapshot.message)
        self.message_label.setProperty("level", snapshot.message_level)
        self.start_button.setEnabled(snapshot.start_enabled)
        self.stop_button.setEnabled(snapshot.stop_enabled)

    def _sync_click_loop(self) -> None:
        if self._click_loop_controller is not None:
            self._click_loop_controller.sync_with_automation()

    def _sync_target_window(self, target_window: str) -> None:
        index = self.target_window_select.findText(target_window, Qt.MatchFixedString)
        if index == -1:
            self.target_window_select.addItem(target_window)
            index = self.target_window_select.findText(target_window, Qt.MatchFixedString)
        self.target_window_select.setCurrentIndex(index)

    @staticmethod
    def _localize_status(status: str) -> str:
        return {
            "ready": "Hazır",
            "running": "Çalışıyor",
            "stopping": "Durduruluyor",
            "stopped": "Durdu",
            "error": "Hata",
        }.get(status, status)


class QTimerClickLoopScheduler:
    """Click loop scheduler backed by a PySide6 QTimer."""

    def __init__(self) -> None:
        self._timer = QTimer()

    def start(self, interval_ms: int, callback: Callable[[], None]) -> None:
        self._timer.stop()
        try:
            self._timer.timeout.disconnect()
        except RuntimeError:
            pass
        self._timer.setInterval(interval_ms)
        self._timer.timeout.connect(callback)
        self._timer.start()

    def stop(self) -> None:
        self._timer.stop()
