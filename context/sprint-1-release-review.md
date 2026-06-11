# TASK-023 — Sprint-1 Release Review

## Karar Özeti

Sprint-1 teknik temel açısından güçlü tamamlandı; ancak ürün release edilmeye
hazır değildir.

MVP kabulü için ana bloklayıcı Windows üzerinde gerçek uçtan uca manuel smoke
testin tamamlanmamış olmasıdır. BUG-001 CPS UI reset problemi çözülmüştür.
macOS tarafında gerçek mouse backend'i oluşturulmuştur, ancak macOS global
hotkey, paketleme, izin deneyimi ve ürün ayarları Sprint-2 kapsamına kalmıştır.

## Tamamlanan Görevler

- TASK-002 — Ana Yüzey Bilgi Mimarisi
- TASK-003 — Hız Ayarı Kuralları
- TASK-004 — Sol Tıklama Motoru, domain temeli kısmi tamamlandı
- TASK-005 — Start / Stop Durum Makinesi
- TASK-006 — Global Kısayol Başlat / Durdur Akışı
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
- TASK-022 — macOS Real Mouse Backend

## Kalan Görevler

### Sprint-1 Bloklayıcı

- TASK-021 — Windows MVP Manuel Smoke Test

Bu görev Windows ortamı gerektirdiği için mevcut `darwin` ortamında
tamamlanamamıştır. MVP kabul kararı bu testten önce verilmemelidir.

### Çözülen Release Bugları

- BUG-001 — CPS değeri UI'da 10'a geri dönüyordu. Seçili CPS artık UI refresh sırasında korunur.

### Eski / Gözden Geçirilecek

- TASK-001 — MVP Kabul Çerçevesini Netleştir

TASK-012 güncel kapsam kapanış kontrolünü yaptığı için TASK-001 artık tarihsel
bir planlama kalıntısıdır. Sprint-2 başlangıcında kapatılmalı veya arşivlenmelidir.

### Sprint-1 Dışı / Opsiyonel

- TASK-007 — Pencere Listeleme ve Hedef Seçimi
- TASK-008 — Pencere Değişince Durdurma Davranışı

Ürün sahibi kararına göre pencere seçimi ve pencere koruması opsiyoneldir;
MVP çıkışını bloklamamalıdır.

## Teknik Borçlar

- Windows gerçek davranışları CI/unit test ile doğrulanamıyor; manuel smoke test şart.
- macOS gerçek davranışı Accessibility/Input Monitoring izinlerine bağlı; izin deneyimi UI'da daha açık hale getirilmeli.
- macOS global hotkey gerçek adapter'ı henüz yok.
- Click loop QTimer ile çalışıyor; uzun vadede worker/thread sınırı ve UI thread güvenliği tekrar gözden geçirilmeli.
- Platform adapter hata sınıflandırması temel seviyede; hata kodu/türü ayrımı ileride netleşmeli.
- Ayarlar kalıcı değil; CPS, hotkey ve pencere seçenekleri uygulama kapanınca kaybolur.
- Profil sistemi yok.
- Paketleme, installer, imzalama ve dağıtım süreci yok.
- Manuel test sonuçları platform bazında standardize edilmeye başladı ama release checklist henüz otomatik değil.

## Sprint-2 Önerileri

### P0 — Release Bloklayıcıları

1. TASK-021 — Windows MVP Manuel Smoke Test
2. Windows smoke test sonucuna göre kritik hata düzeltmeleri
3. macOS gerçek mouse backend smoke test
4. macOS izin eksikliği mesajlarının UI'da doğrulanması

### P1 — Platform Tamamlama

1. macOS OS Global Hotkey Adapter
2. macOS F8 manuel smoke test
3. Windows ve macOS adapter hata mesajlarının ortak kullanıcı diliyle hizalanması

### P2 — Ürünleşme

1. Packaging / installer stratejisi
2. Windows installer
3. macOS app bundle, imzalama ve notarization araştırması
4. README kurulum ve izin yönergeleri

### P3 — Kullanıcı Ayarları

1. CPS ve hotkey ayarlarını kaydetme
2. Son kullanılan pencere koruması ayarını kaydetme
3. Basit ayar dosyası veya platform uyumlu config konumu

### P4 — Güvenlik ve Kontrol

1. Pencere listeleme ve hedef seçimi
2. Pencere değişince durdurma
3. Hedef pencere kapanırsa durdurma
4. Bu davranışlar için manuel kabul senaryolarını güncelleme

### P5 — Büyüme Hazırlığı

1. Profil sistemi
2. Birden fazla tıklama profili
3. Sağ tık / çift tık seçenekleri
4. Makro kayıt ve otomasyon senaryoları için ürün keşfi

## Önceliklendirme

1. Windows MVP manuel smoke test yapılmadan release kararı verilmemeli.
2. macOS backend geliştirmesi tamamlandı; ancak macOS release iddiası için global hotkey ve izin deneyimi tamamlanmalı.
3. Packaging/installer, MVP kabulünden sonra Sprint-2'nin en yüksek ürünleşme önceliği olmalı.
4. Ayar kaydetme, gerçek kullanıcı deneyimi için packaging sonrası hemen ele alınmalı.
5. Profil sistemi ve pencere koruması değerli ama MVP release bloklayıcısı değil.

## Test Durumu

Son unit test sonucu:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests/unit
```

Sonuç: 106 test başarılı.

## Release Tavsiyesi

Sprint-1, teknik temel sprinti olarak başarılıdır. Ürün release edilmemelidir.

Release için minimum sonraki adım:

- Windows üzerinde TASK-021 manuel smoke test çalıştırılsın.
- Bloklayıcı hata çıkmazsa MVP kabul kararı yeniden değerlendirilsin.
- Bloklayıcı hata çıkarsa Sprint-2 P0 hata düzeltme görevleri açılsın.

## PM Brain V2 Notu

Sprint-1 release review sonrasi PM Brain V2 aktif hale getirildi.

- Product Owner Agent: ürün eksikleri ve release recommendation üretir.
- QA Agent: test kapsami, smoke test ve bug raporlari üretir.
- Release Agent: Go/No-Go, platform riskleri ve release blockers takip eder.

Aktif takip dosyalari:

- `.brain/health_report.md`
- `.brain/open_risks.md`
- `.brain/manual_validation.md`
- `.brain/release_status.md`
- `tasks/user-tests/`
- `reviews/product-review-2026-06-11.md`

## PM Brain V2.1 Karar Motoru

`devam et` komutu artik sadece siradaki task'i secmez. Once health report,
open risks, release status, manual validation ve user-test durumlari okunur.

Mevcut karar motoru sonucu:

- Open bug: Yok
- High risk: Windows smoke test eksik
- Release readiness: 78%
- Windows readiness: 70%
- macOS readiness: 85%
- Release status: No-Go
- Suggested next action: TASK-021 — Windows MVP Manuel Smoke Test
