# Kapanis Ozeti

- Durum: Done
- Tamamlanma ozeti: `HotkeyService` app katmaninda olusturuldu; varsayilan F8 tetiklenince otomasyon duruyorsa start, calisiyorsa `HOTKEY_STOPPED` reason ile stop davranisi saglandi. Gecersiz kisa yollar reddediliyor.
- Degisen dosyalar:
  - `src/turkuaz_clickflow/app/hotkey_service.py`
  - `tests/unit/test_hotkey_service.py`
- Test sonucu: `PYTHONPATH=src python3 -m unittest discover -s tests/unit` — 31 test basarili.
- Kapsam disi birakilanlar: OS seviyesinde global hotkey kaydi, Windows/macOS adapter, UI, mouse tiklama motoru.

# TASK-006 — Global Kısayol Başlat / Durdur Akışını Planla ve Geliştir

## Epic

EPIC-03 — Güvenli Başlatma / Durdurma ve Kısayol

## Amaç

Kullanıcının uygulama odağı dışındayken de otomasyonu güvenli şekilde başlatıp durdurabilmesini sağlamak.

## Geliştirici Görevleri

- Tek global kısayolun başlat/durdur toggle davranışını tanımla.
- Geçersiz veya kullanılamayan kısayol durumlarını ele al.
- Kısayol ile Stop komutunun öncelikli çalışmasını sağla.
- Kısayol değişikliğinin ne zaman geçerli olacağını belirle.

## Kabul Kriterleri

- Kısayol otomasyon duruyorken başlatır.
- Kısayol otomasyon çalışıyorken durdurur.
- Kısayol kullanılamıyorsa kullanıcı uyarılır ve otomasyon sessizce başlamaz.
- Kısayol davranışı Start / Stop buton davranışıyla tutarlıdır.

## Bağımlılıklar

- TASK-005

## Önerilen Sıra

6
