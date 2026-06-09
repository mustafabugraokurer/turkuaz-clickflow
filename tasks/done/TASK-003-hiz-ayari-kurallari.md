# Kapanis Ozeti

- Durum: Done
- Tamamlanma ozeti: CPS domain kurallari kodlandi; minimum 1, maksimum 100 ve varsayilan 10 degeri dogrulandi.
- Degisen dosyalar:
  - `pyproject.toml`
  - `README.md`
  - `src/turkuaz_clickflow/__init__.py`
  - `src/turkuaz_clickflow/main.py`
  - `src/turkuaz_clickflow/domain/cps_policy.py`
  - `src/turkuaz_clickflow/domain/automation_settings.py`
  - `tests/unit/test_cps_policy.py`
- Test sonucu: `PYTHONPATH=src python3 -m unittest discover -s tests/unit` — 16 test basarili.
- Kapsam disi birakilanlar: UI, mouse tiklama, global hotkey, platform adapter.

# TASK-003 — Hız Ayarı Kurallarını Tanımla

## Epic

EPIC-02 — Tıklama Motoru ve Hız Kontrolü

## Amaç

Kullanıcının tıklama hızını güvenli ve anlaşılır biçimde ayarlamasını sağlayacak ürün kurallarını belirlemek.

## Geliştirici Görevleri

- Hız giriş biçimini tanımla: saniyedeki tıklama sayısı veya tıklamalar arası bekleme.
- Minimum ve maksimum kabul edilebilir değerleri ürün kararı olarak belirle.
- Geçersiz değerlerde gösterilecek uyarı davranışını tanımla.
- Hız değişikliğinin otomasyon çalışırken mi, yalnızca duruyorken mi uygulanacağını netleştir.

## Kabul Kriterleri

- Geçerli hız aralığı bellidir.
- Geçersiz hızla otomasyon başlatılamaz.
- Kullanıcı hatalı değeri nasıl düzelteceğini anlar.

## Bağımlılıklar

- TASK-001
- TASK-002

## Önerilen Sıra

3
