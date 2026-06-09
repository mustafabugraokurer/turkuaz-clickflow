# Kapanış Özeti

## Durum

Done

## Tamamlanma Özeti

PySide6 Start / Stop ve OS F8 hotkey akışı ClickRunner çalışma döngüsüne
bağlandı. `ClickLoopController` app katmanında UI event loop'u kilitlemeden
periyodik tıklama tick'lerini yönetir. PySide6 tarafında QTimer scheduler
kullanılır; unit testlerde fake scheduler ile gerçek timer veya gerçek mouse
tıklaması üretmeden davranış doğrulanır. Runner hataları `StopReason.ERROR`
feedback mesajına bağlanır.

## Değişen Dosyalar

- `src/turkuaz_clickflow/app/click_loop_controller.py`
- `src/turkuaz_clickflow/app/global_hotkey_controller.py`
- `src/turkuaz_clickflow/ui/viewmodels/main_window_viewmodel.py`
- `src/turkuaz_clickflow/ui/views/main_window.py`
- `src/turkuaz_clickflow/main.py`
- `tests/unit/test_click_loop_controller.py`
- `tests/unit/test_global_hotkey_controller.py`
- `context/mvp-scope-closure.md`
- `tests/manual/mvp-acceptance-scenarios.md`

## Test Sonucu

```bash
PYTHONPATH=src python3 -m unittest discover -s tests/unit
```

Sonuç: 92 test başarılı.

## Kapsam Dışı Bırakılanlar

- Pencere koruması
- macOS gerçek hotkey/mouse implementasyonu
- Windows manuel smoke test yürütümü

# TASK-020 — UI ClickRunner Çalışma Döngüsü Bağlantısı

## Epic

EPIC-01 — Uygulama Kontrol Yüzeyi

## Amaç

PySide6 Start / Stop ve F8 akışını ClickRunner ile bağlayarak kullanıcı
durdurana kadar çalışan tıklama döngüsünü oluşturmak.

## Geliştirici Görevleri

- Start sonrası ClickRunner çalışma döngüsünü başlat.
- UI event loop'unu kilitlemeden tıklama üret.
- Stop butonu ve F8 ile döngüyü güvenli durdur.
- Sayaç ve süre göstergelerini çalışma sırasında güncelle.
- Runner hatalarında `StopReason.ERROR` ve FeedbackService mesajını UI'a yansıt.

## Kabul Kriterleri

- Start sonrası gerçek runner çalışır.
- Stop sonrası yeni tıklama üretilmez.
- F8 çalışırken otomasyonu durdurur.
- UI donmadan sayaç ve süre güncellenir.
- Geçersiz CPS veya adapter hatası kullanıcıya net mesaj gösterir.

## Bağımlılıklar

- TASK-016
- TASK-017
- TASK-019

## Kapsam Dışı

- Pencere koruması
- macOS gerçek hotkey/mouse implementasyonu

## Önerilen Sıra

20
