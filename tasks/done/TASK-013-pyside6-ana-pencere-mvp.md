# Kapanis Ozeti

- Durum: Done
- Tamamlanma ozeti: PySide6 ana pencere iskeleti, wireframe'e uygun temel alanlar ve MainWindowViewModel eklendi. UI, app/domain servislerinden gelen snapshot degerlerini yansitacak sekilde kuruldu.
- Degisen dosyalar:
  - `src/turkuaz_clickflow/main.py`
  - `src/turkuaz_clickflow/ui/__init__.py`
  - `src/turkuaz_clickflow/ui/viewmodels/__init__.py`
  - `src/turkuaz_clickflow/ui/views/__init__.py`
  - `src/turkuaz_clickflow/ui/viewmodels/main_window_viewmodel.py`
  - `src/turkuaz_clickflow/ui/views/main_window.py`
  - `tests/unit/test_main_window_viewmodel.py`
- Test sonucu: `PYTHONPATH=src python3 -m unittest discover -s tests/unit` — 51 test basarili. Gercek PySide6 pencere runtime'i bu ortamda calistirilmadi.
- Kapsam disi birakilanlar: Gercek mouse tiklama, OS seviyesinde global hotkey, platform adapter implementasyonu, UI ile Start/Stop komut baglantisi.

# TASK-013 — PySide6 Ana Pencere MVP

## Epic

EPIC-01 — Uygulama Kontrol Yüzeyi

## Amaç

TASK-002 wireframe'ine uygun, Sprint-1 MVP için kullanılabilir PySide6 ana pencereyi oluşturmak.

## Geliştirici Görevleri

- PySide6 ana pencere iskeletini oluştur.
- Başlık, durum, Start, Stop, CPS, F8, sayaç, çalışma süresi ve mesaj alanlarını ekle.
- Hedef pencere seçimi ve pencere koruması alanlarını opsiyonel/geleceğe hazır şekilde konumlandır.
- UI içinde iş kuralı yazmadan app servislerinden gelen durumu yansıtacak yapı kur.
- Ana pencerenin Windows ve macOS ortak UI kararına uygun kalmasını sağla.

## Kabul Kriterleri

- Uygulama PySide6 ana pencere ile açılır.
- Varsayılan CPS `10`, kısayol `F8` olarak görünür.
- Hazır, çalışıyor, durdu ve hata mesaj alanları gösterilebilir.
- Start/Stop kontrolleri görsel olarak ayırt edilebilir.
- UI katmanı domain/app iş kurallarını kopyalamaz.

## Bağımlılıklar

- TASK-002
- TASK-010

## Kapsam Dışı

- Gerçek mouse tıklama
- OS seviyesinde global hotkey
- Platform adapter implementasyonu

## Önerilen Sıra

13
