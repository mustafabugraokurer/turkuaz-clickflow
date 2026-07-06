"""User-facing status and warning messages."""

from dataclasses import dataclass
from typing import Optional

from turkuaz_clickflow.app.automation_service import AutomationCommandResult
from turkuaz_clickflow.app.hotkey_service import HotkeyResult
from turkuaz_clickflow.domain.automation_state import AutomationState
from turkuaz_clickflow.domain.stop_reason import StopReason


@dataclass(frozen=True)
class FeedbackMessage:
    """A short message that can be shown by the UI layer."""

    level: str
    text: str


class FeedbackService:
    """Builds action-oriented messages from app/domain state."""

    _STATE_MESSAGES = {
        AutomationState.READY: "Hazır. Başlatmak için Start'a basın veya F8 kullanın.",
        AutomationState.RUNNING: "Çalışıyor. Durdurmak için Stop'a basın veya F8 kullanın.",
        AutomationState.STOPPING: "Durduruluyor...",
        AutomationState.STOPPED: "Durdu.",
        AutomationState.ERROR: "Hata oluştu. Ayarları kontrol edip tekrar deneyin.",
    }

    _STOP_REASON_MESSAGES = {
        StopReason.USER_STOPPED: "Durdu. Son durma sebebi: Kullanıcı durdurdu.",
        StopReason.HOTKEY_STOPPED: "Durdu. Son durma sebebi: F8 ile durduruldu.",
        StopReason.INVALID_SETTINGS: "CPS değeri 1 ile 100 arasında olmalıdır.",
        StopReason.WINDOW_CHANGED: "Durdu. Son durma sebebi: Pencere değişti.",
        StopReason.TARGET_WINDOW_MISSING: "Durdu. Son durma sebebi: Hedef pencere bulunamadı.",
        StopReason.ERROR: "Hata nedeniyle durdu. Lütfen tekrar deneyin.",
    }

    def for_state(self, state: AutomationState) -> FeedbackMessage:
        """Return the default message for a lifecycle state."""
        level = "error" if state is AutomationState.ERROR else "info"
        return FeedbackMessage(level=level, text=self._STATE_MESSAGES[state])

    def for_stop_reason(self, reason: StopReason) -> FeedbackMessage:
        """Return a user-facing message for a stop reason."""
        level = "warning" if reason in self._warning_reasons() else "info"
        if reason is StopReason.ERROR:
            level = "error"
        return FeedbackMessage(level=level, text=self._STOP_REASON_MESSAGES[reason])

    def for_automation_result(
        self, result: AutomationCommandResult
    ) -> FeedbackMessage:
        """Return the best user-facing message for an automation command result."""
        if result.stop_reason is not None:
            return self.for_stop_reason(result.stop_reason)
        if result.started:
            return self.for_state(AutomationState.RUNNING)
        if result.stopped:
            return self.for_state(AutomationState.STOPPED)
        if not result.accepted:
            return FeedbackMessage(
                level="warning",
                text=result.message or "İşlem başlatılamadı. Ayarları kontrol edin.",
            )
        return self.for_state(result.state)

    def for_hotkey_result(self, result: HotkeyResult) -> FeedbackMessage:
        """Return a user-facing message for a hotkey trigger result."""
        if not result.accepted:
            if self._is_permission_error(result.message):
                return self.for_platform_error(result.message, operation="hotkey")
            return FeedbackMessage(
                level="warning",
                text="Kısayol kullanılamıyor. F8 başka bir uygulama tarafından kullanılıyor olabilir.",
            )
        if result.automation_result is not None:
            return self.for_automation_result(result.automation_result)
        return FeedbackMessage(level="info", text=result.message)

    def current_message(
        self,
        state: AutomationState,
        stop_reason: Optional[StopReason] = None,
    ) -> FeedbackMessage:
        """Return stop reason message when present, otherwise the state message."""
        if stop_reason is not None:
            return self.for_stop_reason(stop_reason)
        return self.for_state(state)

    def for_platform_error(
        self,
        error_message: str,
        *,
        operation: str = "generic",
    ) -> FeedbackMessage:
        """Return an action-oriented message for platform adapter failures."""
        normalized = error_message.lower()
        if self._is_permission_error(error_message):
            if operation == "hotkey":
                return FeedbackMessage(
                    level="warning",
                    text=(
                        "macOS Input Monitoring izni gerekli olabilir. Sistem "
                        "Ayarları > Gizlilik ve Güvenlik > Input Monitoring "
                        "bölümünden uygulamaya izin verin."
                    ),
                )
            if operation == "mouse":
                return FeedbackMessage(
                    level="warning",
                    text=(
                        "macOS Accessibility izni gerekli olabilir. Sistem "
                        "Ayarları > Gizlilik ve Güvenlik > Accessibility "
                        "bölümünden uygulamaya izin verin."
                    ),
                )
            if "input monitoring" in normalized:
                return FeedbackMessage(
                    level="warning",
                    text=(
                        "macOS Input Monitoring izni gerekli olabilir. Sistem "
                        "Ayarları > Gizlilik ve Güvenlik > Input Monitoring "
                        "bölümünden uygulamaya izin verin."
                    ),
                )
            if "accessibility" in normalized:
                return FeedbackMessage(
                    level="warning",
                    text=(
                        "macOS Accessibility izni gerekli olabilir. Sistem "
                        "Ayarları > Gizlilik ve Güvenlik > Accessibility "
                        "bölümünden uygulamaya izin verin."
                    ),
                )
            return FeedbackMessage(
                level="warning",
                text=(
                    "macOS Accessibility veya Input Monitoring izni gerekli "
                    "olabilir. Sistem Ayarları > Gizlilik ve Güvenlik "
                    "bölümünden uygulamaya izin verin."
                ),
            )

        if self._is_unavailable_backend_error(error_message):
            return FeedbackMessage(
                level="error",
                text="Bu platformda otomasyon backend'i kullanılamıyor.",
            )

        return FeedbackMessage(
            level="error",
            text=f"İşlem başlatılamadı: {error_message}",
        )

    @staticmethod
    def _warning_reasons() -> set:
        return {
            StopReason.INVALID_SETTINGS,
            StopReason.WINDOW_CHANGED,
            StopReason.TARGET_WINDOW_MISSING,
        }

    @staticmethod
    def _is_permission_error(error_message: str) -> bool:
        normalized = error_message.lower()
        return (
            "accessibility" in normalized
            or "input monitoring" in normalized
            or "permission" in normalized
            or "izin" in normalized
        )

    @staticmethod
    def _is_unavailable_backend_error(error_message: str) -> bool:
        normalized = error_message.lower()
        return (
            "not available" in normalized
            or "not implemented" in normalized
            or "unavailable" in normalized
            or "api is not available" in normalized
            or ("backend" in normalized and "kullanılamıyor" in normalized)
        )
