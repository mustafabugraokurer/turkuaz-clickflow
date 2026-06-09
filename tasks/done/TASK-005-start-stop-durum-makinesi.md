# Kapanis Ozeti

- Durum: Done
- Tamamlanma ozeti: `AutomationService` ile start/stop durum makinesi app katmaninda kuruldu; tekrar start engellendi, stop guvenli kabul edildi ve stop reason uretimi eklendi.
- Degisen dosyalar:
  - `src/turkuaz_clickflow/app/__init__.py`
  - `src/turkuaz_clickflow/app/automation_service.py`
  - `tests/unit/test_automation_service.py`
- Test sonucu: `PYTHONPATH=src python3 -m unittest discover -s tests/unit` — 25 test basarili.
- Kapsam disi birakilanlar: UI, mouse tiklama motoru, global hotkey implementasyonu, platform adapter.

# TASK-005 — Start / Stop Durum Makinesini Tanımla

## Epic

EPIC-03 — Güvenli Başlatma / Durdurma ve Kısayol

## Amaç

Otomasyonun hazır, çalışıyor, durduruluyor, durdu ve hata durumları arasında kontrollü geçmesini sağlamak.

## Geliştirici Görevleri

- Otomasyon yaşam döngüsü durumlarını tanımla.
- Start için gerekli ön koşulları listele.
- Stop komutunun tüm durumlarda nasıl ele alınacağını belirle.
- Çalışırken tekrar start verilmesini engelle.
- Durma sebebi üretimini durum geçişlerine bağla.

## Kabul Kriterleri

- Aynı anda iki otomasyon döngüsü başlatılamaz.
- Stop komutu çalışırken her zaman kabul edilir.
- Her durma için kullanıcıya gösterilebilir bir sebep üretilir.

## Bağımlılıklar

- TASK-002
- TASK-004

## Önerilen Sıra

5
