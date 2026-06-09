# Sprint-1 Çıktısı

## Sprint Hedefi

Windows masaüstünde çalışan ilk minimum auto clicker sürümünü üretmek ve macOS desteği için temel mimari uyumluluk hazırlığını korumak.

Kullanıcı, uygulamayı açtıktan sonra varsayılan `10 CPS` hızla sol tıklama otomasyonunu başlatabilmeli, `F8` veya Stop kontrolüyle durdurabilmeli ve her yeni çalıştırmada sıfırdan başlayan tıklama sayacını görebilmelidir.

## Sprint-1 Ürün Kararları

- Minimum CPS: 1
- Maksimum CPS: 100
- Varsayılan CPS: 10
- Varsayılan global kısayol: `F8`
- Yeni çalıştırmada sayaç sıfırlanır
- Pencere seçimi isteğe bağlıdır
- Pencere koruması opsiyoneldir
- Ürün Windows ve macOS destekleyecek şekilde tasarlanır
- İlk geliştirme Windows odaklı yapılabilir
- macOS için temel uyumluluk hazırlığı mimaride baştan düşünülür
- Mouse, klavye ve pencere işlemleri platform adapter yapısına ayrılır
- MVP teknolojisi Python'dır
- UI için PySide6 kullanılır

## Platform Mimari Kabulü

- Windows ve macOS aynı arayüzü kullanır.
- Ortak ürün mantığı, sayaç, durum makinesi ve UI platformdan bağımsızdır.
- Pencere listeleme, global kısayol ve otomatik tıklama işletim sistemine göre ayrı uygulanır.
- Windows adapter ve macOS adapter sınırları ürün planında görünür olmalıdır.
- Sprint-1 Windows odaklı ilerleyebilir; macOS adapter tam uygulaması Sprint-1 bloklayıcısı değildir.
- PySide6 UI katmanı, domain ve uygulama katmanından ayrıdır.

## Seçilen Minimum Görevler

### 1. TASK-001 — MVP Kabul Çerçevesini Netleştir

Sprint-1'in Windows odaklı auto clicker çekirdeği olarak kabul edileceğini ve macOS uyumluluk hazırlığının mimaride dikkate alınacağını netleştirir.

### 2. TASK-002 — Ana Yüzey Bilgi Mimarisini Tanımla

Start / Stop, CPS ayarı, kısayol, sayaç, süre ve durum alanlarının davranışını belirler.

### 3. TASK-003 — Hız Ayarı Kurallarını Tanımla

1-100 CPS aralığını ve 10 CPS varsayılanını sprint kabul kuralı yapar.

### 4. TASK-004 — Sol Tıklama Motorunu Planla ve Geliştir

Belirlenen CPS değerine göre sol tık üreten temel motoru kapsar.

### 5. TASK-005 — Start / Stop Durum Makinesini Tanımla

Otomasyonun güvenli şekilde başlamasını, durmasını ve tekrar start çakışmalarını engeller.

### 6. TASK-006 — Global Kısayol Başlat / Durdur Akışını Planla ve Geliştir

Varsayılan `F8` kısayoluyla başlatma ve durdurma davranışını kapsar.

### 7. TASK-009 — Sayaç ve Çalışma Süresi

Her yeni çalıştırmada sıfırlanan sayaç ve çalışma süresi göstergesini kapsar.

### 8. TASK-010 — Durum, Uyarı ve Durma Sebebi Mesajları

Hazır, çalışıyor, durdu, hata ve kullanıcıya gösterilecek durma sebebi mesajlarını kapsar.

### 9. TASK-011 — MVP Manuel Doğrulama Senaryoları

Sprint-1 kabulü için manuel doğrulama senaryolarını üretir.

### 10. TASK-012 — MVP Kapsam Kapanış Kontrolü

Sprint sonunda minimum kapsamın tamamlandığını ve bloklayıcı kalmadığını kontrol eder.

## Sprint-1'e Alınmayan Görevler

### TASK-007 — Pencere Listeleme ve Hedef Seçimi

Pencere seçimi ürün için değerlidir, fakat ürün sahibi kararına göre isteğe bağlıdır. Sprint-1 minimum çıkışını engellemez.

### TASK-008 — Pencere Değişince Durdurma Davranışı

Pencere koruması güvenlik açısından değerlidir, fakat ürün sahibi kararına göre opsiyoneldir. Sprint-1 minimum çıkışını engellemez.

## Görev Bağımlılıkları

- TASK-001 başlangıç görevidir.
- TASK-002, TASK-001 sonrası yapılır.
- TASK-003, TASK-001 ve TASK-002 sonrası yapılır.
- TASK-004, TASK-003 sonrası yapılır.
- TASK-005, TASK-002 ve TASK-004 sonrası yapılır.
- TASK-006, TASK-005 sonrası yapılır.
- TASK-009, TASK-004 ve TASK-005 sonrası yapılır.
- TASK-010, TASK-005, TASK-006 ve TASK-009 sonrası yapılır.
- TASK-011, TASK-003, TASK-006 ve TASK-010 sonrası yapılır.
- TASK-012, TASK-011 sonrası yapılır.

## Önerilen Geliştirme Sırası

1. TASK-001 — MVP Kabul Çerçevesi
2. TASK-002 — Ana Yüzey Bilgi Mimarisi
3. TASK-003 — CPS Hız Kuralları
4. TASK-004 — Sol Tıklama Motoru
5. TASK-005 — Start / Stop Durum Makinesi
6. TASK-006 — `F8` Global Kısayol
7. TASK-009 — Sayaç ve Çalışma Süresi
8. TASK-010 — Durum ve Durma Sebebi Mesajları
9. TASK-011 — Manuel Doğrulama Senaryoları
10. TASK-012 — Kapsam Kapanış Kontrolü

## Sprint-1 Kabul Kriterleri

- Uygulama Sprint-1'de Windows masaüstü hedefiyle değerlendirilir.
- Ürün mimarisi Windows ve macOS desteğine hazırlanacak şekilde değerlendirilir.
- Mouse, klavye, pencere listeleme, global kısayol ve otomatik tıklama işlemleri platform adapter sınırlarıyla ayrılır.
- Varsayılan hız 10 CPS olur.
- Kullanıcı CPS değerini 1 ile 100 arasında ayarlayabilir.
- 1'in altı veya 100'ün üstü CPS değerleriyle otomasyon başlatılmaz.
- Start kontrolü otomasyonu başlatır.
- Stop kontrolü otomasyonu durdurur.
- `F8` otomasyon duruyorken başlatır, çalışıyorken durdurur.
- Yeni çalıştırmada tıklama sayacı sıfırlanır.
- Stop sonrası son sayaç ve çalışma süresi kullanıcıya görünür kalır.
- Kullanıcı otomasyonun hazır, çalışıyor, durdu veya hata durumunu anlayabilir.
- Pencere seçimi yapılmadan otomasyon başlatılabilir.
- OCR, görüntü tanıma, makro kaydı ve klavye otomasyonu Sprint-1 kapsamında değildir.
