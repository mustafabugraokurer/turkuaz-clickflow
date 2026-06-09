# Kapanis Ozeti

- Durum: Done
- Tamamlanma ozeti: `FeedbackService` eklendi; hazir, calisiyor, durduruluyor, durdu ve hata durumlari ile stop reason mesajlari kullanici odakli metinlere cevrildi.
- Degisen dosyalar:
  - `src/turkuaz_clickflow/app/feedback_service.py`
  - `tests/unit/test_feedback_service.py`
- Test sonucu: `PYTHONPATH=src python3 -m unittest discover -s tests/unit` — 49 test basarili.
- Kapsam disi birakilanlar: PySide6 UI, platform adapter, gercek OS hotkey, mouse tiklama motoru.

# TASK-010 — Durum, Uyarı ve Durma Sebebi Mesajları

## Epic

EPIC-05 — Sayaç, Süre ve Durma Sebebi

## Amaç

Kullanıcının otomasyonun mevcut durumunu ve gerektiğinde ne yapması gerektiğini anlamasını sağlamak.

## Geliştirici Görevleri

- Hazır, çalışıyor, durdu ve hata mesajlarını tanımla.
- Stop, kısayol, pencere değişimi, geçersiz ayar ve hata durma sebeplerini listele.
- Kullanıcı aksiyonuna odaklanan kısa uyarı metinleri hazırla.
- Hata mesajlarının otomasyonu güvenli durdurma davranışıyla uyumunu doğrula.

## Kabul Kriterleri

- Her durma sebebi kullanıcıya anlaşılır şekilde gösterilir.
- Geçersiz ayarlarda kullanıcı neyi düzeltmesi gerektiğini anlar.
- Hata mesajları teknik ayrıntıya boğulmaz.

## Bağımlılıklar

- TASK-005
- TASK-006
- TASK-008
- TASK-009

## Önerilen Sıra

10
