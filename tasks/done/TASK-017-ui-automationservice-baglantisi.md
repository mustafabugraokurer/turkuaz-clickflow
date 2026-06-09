# Kapanış Özeti

## Durum

Done

## Tamamlanma Özeti

PySide6 ana pencere kontrolleri viewmodel üzerinden app servislerine bağlandı.
Start komutu CPS değerini `AutomationService` validasyonuna iletir, Stop komutu
güvenli durdurma akışını çalıştırır, F8 tetikleme akışı `HotkeyService`
üzerinden test edilebilir hale geldi. Snapshot artık sayaç, süre, feedback
mesajı ve Start/Stop aktiflik durumunu servis state'inden üretir.

## Değişen Dosyalar

- `src/turkuaz_clickflow/ui/viewmodels/main_window_viewmodel.py`
- `src/turkuaz_clickflow/ui/views/main_window.py`
- `tests/unit/test_main_window_viewmodel.py`

## Test Sonucu

```bash
PYTHONPATH=src python3 -m unittest discover -s tests/unit
```

Sonuç: 75 test başarılı.

## Kapsam Dışı Bırakılanlar

- OS seviyesinde global hotkey
- Pencere koruması
- Gerçek OS seviyesinde mouse tıklama backend'i
- Manuel PySide6 görsel doğrulama

# TASK-017 — UI ile AutomationService Bağlantısı

## Epic

EPIC-01 — Uygulama Kontrol Yüzeyi

## Amaç

PySide6 ana pencere kontrollerini AutomationService, HotkeyService, TimerService ve FeedbackService ile bağlamak.

## Geliştirici Görevleri

- Start butonunu AutomationService start komutuna bağla.
- Stop butonunu AutomationService stop komutuna bağla.
- CPS girişini domain validasyonuna bağla.
- Sayaç ve çalışma süresi göstergelerini app servislerinden güncelle.
- FeedbackService mesajlarını UI mesaj alanında göster.
- UI durumuna göre Start/Stop aktiflik davranışını güncelle.

## Kabul Kriterleri

- Start butonu otomasyonu app seviyesinde başlatır.
- Stop butonu otomasyonu app seviyesinde durdurur.
- Geçersiz CPS kullanıcıya net mesaj gösterir.
- Sayaç ve süre UI'da güncellenir.
- UI iş kurallarını kopyalamadan app/domain servislerini kullanır.

## Bağımlılıklar

- TASK-013
- TASK-005
- TASK-009
- TASK-010
- TASK-016

## Kapsam Dışı

- OS seviyesinde global hotkey
- Pencere koruması

## Önerilen Sıra

17
