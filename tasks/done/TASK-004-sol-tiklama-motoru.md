# Kapanis Ozeti

- Durum: Kismi Done
- Tamamlanma ozeti: Sol tiklama motorunun domain temeli hazirlandi; CPS ayarlari, sayac, otomasyon durumlari ve durma sebepleri tanimlandi. Gercek mouse tiklama dongusu henuz yazilmadi.
- Degisen dosyalar:
  - `src/turkuaz_clickflow/domain/cps_policy.py`
  - `src/turkuaz_clickflow/domain/automation_state.py`
  - `src/turkuaz_clickflow/domain/automation_settings.py`
  - `src/turkuaz_clickflow/domain/counter.py`
  - `src/turkuaz_clickflow/domain/stop_reason.py`
  - `tests/unit/test_cps_policy.py`
  - `tests/unit/test_counter.py`
  - `tests/unit/test_automation_state.py`
- Test sonucu: `PYTHONPATH=src python3 -m unittest discover -s tests/unit` — 16 test basarili.
- Kapsam disi birakilanlar: Mouse tiklama implementasyonu, platform adapter, global hotkey, UI.

# TASK-004 — Sol Tıklama Motorunu Planla ve Geliştir

## Epic

EPIC-02 — Tıklama Motoru ve Hız Kontrolü

## Amaç

Belirlenen hızda sol tık üreten temel otomasyon motorunu MVP davranışlarına uygun şekilde geliştirmek.

## Geliştirici Görevleri

- Sol tık üretme akışını tasarla.
- Hız ayarıyla tıklama döngüsü arasındaki ilişkiyi uygula.
- Start komutuyla başlama, Stop komutuyla durma davranışını hazırla.
- Her başarılı tıklama sonrası sayaç olayını üret.
- Hata durumunda güvenli durma sinyali oluştur.

## Kabul Kriterleri

- Motor yalnızca sol tık üretir.
- Seçilen hız davranışı tutarlı çalışır.
- Stop komutu sonrası yeni tıklama üretilmez.
- Sayaç yalnızca gerçekleşen tıklamalarda artar.

## Bağımlılıklar

- TASK-003

## Önerilen Sıra

4
