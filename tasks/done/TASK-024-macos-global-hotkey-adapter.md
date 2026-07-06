# Durum

Tamamlandi.

# Tamamlanma Ozeti

macOS global hotkey adapter eklendi. Varsayilan `F8` kısayolu macOS platform
adapter katmaninda desteklenir hale geldi. Adapter, Quartz key-state polling
backend'i uzerinden callback tetikler ve mevcut `GlobalHotkeyController` akisi
ile uyumludur.

macOS disi ortamlarda real OS cagrisi yapilmadan unavailable backend davranisi
korundu.

# Degisen Dosyalar

- `src/turkuaz_clickflow/platform/macos/hotkey.py`
- `src/turkuaz_clickflow/platform/macos/__init__.py`
- `tests/unit/test_macos_hotkey_adapter.py`
- `tests/unit/test_platform_interfaces.py`
- `.brain/health_report.md`
- `.brain/open_risks.md`
- `.brain/manual_validation.md`
- `.brain/release_status.md`
- `.brain/project_state.md`
- `context/current_sprint.md`
- `tasks/todo/README.md`
- `tasks/done/README.md`

# Test Sonucu

```bash
PYTHONPATH=src python3 -m unittest discover -s tests/unit
```

Sonuc: 128 test basarili.

# Kapsam Disi Birakilanlar

- macOS uzerinde gercek manuel F8 smoke test
- macOS izin UX metinlerinin detayli urun incelemesi
- Packaging / signing / notarization

# TASK-024 - macOS Global Hotkey Adapter

## Epic

EPIC-03 - Global Kisayol ve Guvenli Durdurma

## Amac

macOS uzerinde varsayilan `F8` global kisayolunu platform adapter katmanina
baglayarak otomasyonun uygulama odakta degilken de baslatilip durdurulmasini
saglamak.

## Kabul Sonucu

- macOS adapter `F8` kaydini backend uzerinden baslatabilir.
- Hotkey tetiklenince callback mevcut start/stop akisini tetikleyecek sekilde
  `GlobalHotkeyController` ile uyumludur.
- Kayit basarisiz olursa kullaniciya donulebilecek `PlatformOperationError`
  mesaji uretilir.
- Windows hotkey testlerinde regresyon yoktur.

## Sonraki Onerilen Aksiyon

TASK-027 - macOS Permission UX Review
