# Kapanış Özeti

## Durum

Done

## Tamamlanma Özeti

Windows global hotkey adapter eklendi. Adapter `F8` değerini Windows
`RegisterHotKey` sanal tuş değerine çözer, callback'i platform sınırında tutar
ve backend hatalarını `PlatformOperationError` ile sarar. App katmanında
`GlobalHotkeyController` oluşturuldu; OS adapter callback'lerini `HotkeyService`
üzerinden start/stop toggle akışına yönlendirir ve kayıt başarısız olduğunda
`FeedbackService` ile kullanıcıya uyarı mesajı üretir. macOS global hotkey
placeholder davranışı korunmuştur.

## Değişen Dosyalar

- `src/turkuaz_clickflow/platform/windows/hotkey.py`
- `src/turkuaz_clickflow/platform/windows/__init__.py`
- `src/turkuaz_clickflow/app/global_hotkey_controller.py`
- `src/turkuaz_clickflow/main.py`
- `src/turkuaz_clickflow/ui/viewmodels/main_window_viewmodel.py`
- `tests/unit/test_windows_hotkey_adapter.py`
- `tests/unit/test_global_hotkey_controller.py`
- `tests/unit/test_platform_interfaces.py`

## Test Sonucu

```bash
PYTHONPATH=src python3 -m unittest discover -s tests/unit
```

Sonuç: 85 test başarılı.

## Kapsam Dışı Bırakılanlar

- Mouse tıklama adapter değişiklikleri
- Pencere listeleme
- Pencere koruması
- Makro/OCR/görüntü tanıma
- macOS gerçek global hotkey implementasyonu

# TASK-018 — OS Global Hotkey Adapter

## Epic

EPIC-03 — Güvenli Başlatma / Durdurma ve Kısayol

## Amaç

Windows odaklı gerçek OS global F8 hotkey adapter implementasyonunu oluşturmak ve macOS için temel uyumluluk hazırlığını yapmak.

## Geliştirici Görevleri

- Platform adapter interface'e uygun global hotkey adapter oluştur.
- Windows'ta F8 global kısayol kayıt/dinleme davranışını uygula.
- macOS için destek durumu veya placeholder davranışını netleştir.
- Hotkey tetiklerini HotkeyService'e yönlendir.
- Kısayol kullanılamıyorsa FeedbackService ile kullanıcıya anlaşılır uyarı üretilmesini sağla.

## Kabul Kriterleri

- F8, uygulama odakta değilken de start/stop toggle davranışını tetikler.
- Çalışırken F8 stop reason olarak `HOTKEY_STOPPED` üretir.
- Kısayol kullanılamıyorsa otomasyon sessizce başlamaz.
- OS adapter app/domain iş kurallarını kopyalamaz.

## Bağımlılıklar

- TASK-006
- TASK-014
- TASK-017

## Kapsam Dışı

- Mouse tıklama adapter
- Pencere listeleme
- Makro/OCR/görüntü tanıma

## Önerilen Sıra

18
