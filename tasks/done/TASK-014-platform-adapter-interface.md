# Kapanis Ozeti

- Durum: Done
- Tamamlanma ozeti: Platform adapter interface/protocol katmani eklendi; mouse click, global hotkey, window query ve platform adapter sozlesmeleri tanimlandi. Windows/macOS adapter shell'leri ve platform registry olusturuldu; gercek OS cagrilari kapsam disi birakildi.
- Degisen dosyalar:
  - `src/turkuaz_clickflow/platform/__init__.py`
  - `src/turkuaz_clickflow/platform/interfaces.py`
  - `src/turkuaz_clickflow/platform/unsupported.py`
  - `src/turkuaz_clickflow/platform/windows/__init__.py`
  - `src/turkuaz_clickflow/platform/macos/__init__.py`
  - `src/turkuaz_clickflow/platform/registry.py`
  - `tests/unit/test_platform_interfaces.py`
- Test sonucu: `PYTHONPATH=src python3 -m unittest discover -s tests/unit` — 59 test basarili.
- Kapsam disi birakilanlar: Gercek Windows adapter implementasyonu, gercek macOS adapter implementasyonu, UI, mouse tiklama OS cagrisi, OS global hotkey.

# TASK-014 — Platform Adapter Interface

## Epic

EPIC-04 — Pencere Hedefleme ve Odak Koruması

## Amaç

Windows ve macOS özel işlemleri için ortak adapter sözleşmelerini tanımlamak.

## Geliştirici Görevleri

- Mouse tıklama adapter sözleşmesini tanımla.
- Global hotkey adapter sözleşmesini tanımla.
- Pencere listeleme / aktif pencere adapter sözleşmesini tanımla.
- Platform algılama ve adapter seçimi için temel app/platform sınırını belirle.
- Windows ve macOS klasörlerinin aynı sözleşmeleri uygulayacak şekilde hazırlanmasını sağla.

## Kabul Kriterleri

- Platforma özel işlemler için ortak interface/protocol vardır.
- App katmanı OS detaylarına doğrudan bağımlı değildir.
- Windows ve macOS adapter implementasyonları aynı sözleşmeye bağlanabilir.
- Interface katmanı gerçek OS çağrısı yapmaz.

## Bağımlılıklar

- DEC-005 Platform Desteği ve Adapter Kararı
- TASK-004
- TASK-006

## Kapsam Dışı

- Gerçek Windows adapter implementasyonu
- Gerçek macOS adapter implementasyonu
- UI

## Önerilen Sıra

14
