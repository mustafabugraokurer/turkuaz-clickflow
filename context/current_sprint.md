# Sprint 1

## Amaç

Windows masaüstünde çalışan minimum auto clicker çekirdeğini oluşturmak ve macOS desteği için temel mimari uyumluluk hazırlığını dikkate almak.

Sprint-1 çıktısı; kullanıcının varsayılan `F8` kısayolu veya Start / Stop kontrolüyle otomasyonu başlatıp durdurabildiği, 1-100 CPS aralığında sol tık üretebildiği ve her yeni çalıştırmada sayacı sıfırlanan ilk kullanılabilir sürümdür.

## Ürün Sahibi Kararları

- Minimum CPS: 1
- Maksimum CPS: 100
- Varsayılan CPS: 10
- Varsayılan kısayol: `F8`
- Yeni çalıştırmada sayaç sıfırlanacak
- Pencere seçimi isteğe bağlı olacak
- Pencere koruması opsiyonel olacak
- Ürün Windows ve macOS destekleyecek şekilde tasarlanacak
- İlk geliştirme Windows odaklı yapılabilir
- macOS desteği için temel uyumluluk hazırlığı baştan düşünülecek
- Mouse, klavye ve pencere işlemleri platform adapter yapısına ayrılacak
- MVP teknolojisi Python olacak
- UI için PySide6 kullanılacak

## Sprint-1 Minimum Kapsam

- Windows masaüstü uygulaması olarak MVP kabul çerçevesi
- macOS temel uyumluluk hazırlığı için platform adapter sınırlarının dikkate alınması
- Python + PySide6 kararına uygun proje mimarisi
- Ana kontrol yüzeyi davranışları
- CPS hız ayarı: 1-100 arası, varsayılan 10
- Sol tıklama motoru
- Start / Stop durum akışı
- Global `F8` başlat / durdur kısayolu
- Her yeni çalıştırmada sıfırlanan tıklama sayacı
- Çalışma süresi ve durum bilgisi
- Kullanıcıya anlaşılır uyarı ve durma sebebi mesajları
- Manuel MVP doğrulama senaryoları

## Platform Mimari Notu

- Ortak ürün mantığı, sayaç, durum makinesi ve UI platformdan bağımsız olmalıdır.
- Pencere listeleme, global kısayol ve otomatik tıklama işletim sistemine göre ayrı adapter üzerinden uygulanmalıdır.
- Sprint-1 Windows odaklı ilerleyebilir; macOS adapter için tam uygulama Sprint-1 bloklayıcısı değildir.
- PySide6 yalnızca UI katmanında kalmalı; ürün mantığı PySide6 bağımlılığı taşımamalıdır.

## Sprint-1 Durumu

### Done

- TASK-002 — Ana Yüzey Bilgi Mimarisini Tanımla
- TASK-003 — Hız Ayarı Kurallarını Tanımla
- TASK-004 — Sol Tıklama Motorunu Planla ve Geliştir, domain temeli kısmi tamamlandı
- TASK-005 — Start / Stop Durum Makinesini Tanımla
- TASK-006 — Global Kısayol Başlat / Durdur Akışını Planla ve Geliştir
- TASK-009 — Sayaç ve Çalışma Süresi
- TASK-010 — Durum, Uyarı ve Durma Sebebi Mesajları
- TASK-011 — MVP Manuel Doğrulama Senaryoları
- TASK-012 — MVP Kapsam Kapanış Kontrolü
- TASK-013 — PySide6 Ana Pencere MVP
- TASK-014 — Platform Adapter Interface
- TASK-015 — Mouse Click Adapter
- TASK-016 — Click Runner
- TASK-017 — UI ile AutomationService Bağlantısı
- TASK-018 — OS Global Hotkey Adapter
- TASK-019 — Windows Real Mouse Backend
- TASK-020 — UI ClickRunner Çalışma Döngüsü Bağlantısı

### Todo

- TASK-001 — MVP Kabul Çerçevesini Netleştir
- TASK-021 — Windows MVP Manuel Smoke Test

### Sonraki Önerilen Task

TASK-021 — Windows MVP Manuel Smoke Test

### MVP Kapanış Notu

TASK-012 tamamlandı ve MVP kabul edilmedi. Gerçek MVP kapanışı için Windows uçtan uca manuel smoke test tamamlanmalıdır.

Sıradaki bloklayıcı revizyon görevi TASK-021'dir.

## Sprint-1 Dışı / Opsiyonel

- TASK-007 — Pencere Listeleme ve Hedef Seçimi
- TASK-008 — Pencere Değişince Durdurma Davranışı

Bu iki görev ürün hedefi açısından değerlidir, ancak ürün sahibi kararıyla pencere seçimi ve pencere koruması opsiyonel olduğu için Sprint-1 minimum çıkışının bloklayıcısı değildir.

## Kapsam Dışı

- OCR
- Görüntü tanıma
- Makro kaydı
- Klavye otomasyonu
- Profil sistemi
- Senaryo oluşturucu

## PM Brain Workflow

- Repo talimatlarının ana kaynağı: `AGENTS.md`
- Proje durumu: `.brain/project_state.md`
- Tamamlanan task dosyaları `tasks/done/` altında tutulur.
- Açık task dosyaları `tasks/todo/` altında tutulur.
- Task tamamlandığında sprint durumu, project state ve task README dosyaları güncellenir.
