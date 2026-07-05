"""Windows window enumeration adapter."""

from __future__ import annotations

import ctypes
import os
import sys
from ctypes import wintypes
from typing import List, Optional, Protocol

from turkuaz_clickflow.platform.interfaces import WindowInfo


class WindowsWindowQueryBackend(Protocol):
    """Backend contract for visible top-level desktop windows."""

    def list_window_handles(self) -> List[int]:
        """Return visible window handles."""

    def active_window_handle(self) -> Optional[int]:
        """Return the active window handle."""

    def title_for(self, handle: int) -> str:
        """Return the window title for a handle."""

    def process_name_for(self, handle: int) -> Optional[str]:
        """Return the owning process name, if known."""


class UnavailableWindowsWindowQueryBackend:
    """Backend used when Windows APIs are not available in the current process."""

    def list_window_handles(self) -> List[int]:
        return []

    def active_window_handle(self) -> Optional[int]:
        return None

    def title_for(self, handle: int) -> str:
        return ""

    def process_name_for(self, handle: int) -> Optional[str]:
        return None


class WindowsWindowQueryAdapter:
    """Expose Windows windows as UI-friendly values."""

    def __init__(self, backend: WindowsWindowQueryBackend) -> None:
        self._backend = backend

    def list_windows(self) -> List[WindowInfo]:
        windows = []
        for handle in self._backend.list_window_handles():
            info = self._to_window_info(handle)
            if info is not None:
                windows.append(info)
        return windows

    def active_window(self) -> Optional[WindowInfo]:
        handle = self._backend.active_window_handle()
        if handle is None:
            return None
        return self._to_window_info(handle)

    def _to_window_info(self, handle: int) -> Optional[WindowInfo]:
        title = self._backend.title_for(handle).strip()
        if not title:
            return None
        return WindowInfo(
            id=str(handle),
            title=title,
            process_name=self._backend.process_name_for(handle),
        )


class WindowsUser32WindowQueryBackend:
    """Visible top-level window backend implemented with `user32`."""

    PROCESS_QUERY_LIMITED_INFORMATION = 0x1000

    def __init__(self, user32: object | None = None, kernel32: object | None = None) -> None:
        if user32 is None or kernel32 is None:
            if sys.platform != "win32":
                raise RuntimeError("Windows window query API is not available")
            user32 = user32 or ctypes.windll.user32
            kernel32 = kernel32 or ctypes.windll.kernel32
        self._user32 = user32
        self._kernel32 = kernel32

    def list_window_handles(self) -> List[int]:
        handles: List[int] = []
        enum_proc = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)

        def callback(hwnd: int, _lparam: int) -> bool:
            if self._user32.IsWindowVisible(hwnd) and self.title_for(hwnd).strip():
                handles.append(int(hwnd))
            return True

        self._user32.EnumWindows(enum_proc(callback), 0)
        return handles

    def active_window_handle(self) -> Optional[int]:
        hwnd = int(self._user32.GetForegroundWindow() or 0)
        return hwnd or None

    def title_for(self, handle: int) -> str:
        length = int(self._user32.GetWindowTextLengthW(handle))
        if length <= 0:
            return ""
        buffer = ctypes.create_unicode_buffer(length + 1)
        self._user32.GetWindowTextW(handle, buffer, length + 1)
        return buffer.value

    def process_name_for(self, handle: int) -> Optional[str]:
        process_id = wintypes.DWORD()
        self._user32.GetWindowThreadProcessId(handle, ctypes.byref(process_id))
        if not process_id.value:
            return None

        process_handle = self._kernel32.OpenProcess(
            self.PROCESS_QUERY_LIMITED_INFORMATION,
            False,
            process_id.value,
        )
        if not process_handle:
            return None

        try:
            buffer_length = wintypes.DWORD(260)
            buffer = ctypes.create_unicode_buffer(buffer_length.value)
            if not self._kernel32.QueryFullProcessImageNameW(
                process_handle,
                0,
                buffer,
                ctypes.byref(buffer_length),
            ):
                return None
            return os.path.basename(buffer.value)
        finally:
            self._kernel32.CloseHandle(process_handle)


def create_windows_window_query_backend() -> WindowsWindowQueryBackend:
    """Create the real Windows window-query backend when available."""
    if sys.platform != "win32":
        return UnavailableWindowsWindowQueryBackend()
    return WindowsUser32WindowQueryBackend()
