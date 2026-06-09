# Katmanlı Uygulama Yapısı

## Mimari Yaklaşım

Turkuaz ClickFlow, Python ve PySide6 ile geliştirilecek masaüstü uygulaması olarak planlanır. Ürün Windows ve macOS destekleyecek şekilde tasarlanır; Sprint-1 Windows odaklı ilerleyebilir, ancak macOS uyumluluğu mimari sınırlarla baştan korunur.

## Katmanlar

### 1. UI Katmanı

Konum: `src/turkuaz_clickflow/ui/`

Sorumluluklar:

- PySide6 ana pencere ve ekran bileşenleri
- Start / Stop kontrolleri
- CPS ayarı görünümü
- Sayaç, süre, durum ve uyarı gösterimleri
- Kullanıcı aksiyonlarını uygulama katmanına iletme

UI katmanı iş kuralı içermez. Sayaç hesaplama, durum geçişi, CPS doğrulama ve otomasyon kontrolü bu katmanda yapılmaz.

### 2. Uygulama Katmanı

Konum: `src/turkuaz_clickflow/app/`

Sorumluluklar:

- Use case orkestrasyonu
- Start / Stop akışının yönetimi
- Global kısayoldan gelen komutların yönlendirilmesi
- Tıklama motoru, sayaç ve durum makinesi arasındaki koordinasyon
- Platform adapter seçimi ve kullanımı

Bu katman UI'dan komut alır, domain kurallarını çalıştırır ve platform adapter'larına ihtiyaç duyulan işletim sistemi işlemlerini delege eder.

### 3. Domain Katmanı

Konum: `src/turkuaz_clickflow/domain/`

Sorumluluklar:

- CPS kuralları: minimum 1, maksimum 100, varsayılan 10
- Otomasyon durum makinesi
- Sayaç ve çalışma süresi davranışı
- Durma sebebi modeli
- Otomasyon ayarları ve ürün kavramları

Domain katmanı PySide6 veya işletim sistemi detaylarına bağımlı olmamalıdır.

### 4. Platform Adapter Katmanı

Konum: `src/turkuaz_clickflow/platform/`

Sorumluluklar:

- Otomatik tıklama işlemleri
- Global kısayol kayıt ve dinleme işlemleri
- Pencere listeleme ve aktif pencere kontrolü
- Mouse ve klavye işlemleri

Platform adapter yapısı:

- `platform/windows/` — Windows adapter
- `platform/macos/` — macOS adapter

Sprint-1 Windows odaklı ilerleyebilir. macOS adapter için tam uygulama Sprint-1 bloklayıcısı değildir, ancak arayüz sınırları baştan görünür olmalıdır.

### 5. Config Katmanı

Konum: `src/turkuaz_clickflow/config/`

Sorumluluklar:

- Varsayılan CPS: 10
- Varsayılan kısayol: F8
- Platform ve uygulama sabitleri
- MVP kapsamındaki varsayılan değerler

### 6. Test ve Kabul Katmanı

Konum: `tests/`

Sorumluluklar:

- Domain kuralları için unit test planı
- Uygulama akışları için integration test planı
- Sprint-1 manuel kabul senaryoları

## Bağımlılık Yönü

Beklenen yön:

`UI -> App -> Domain`

`App -> Platform Adapter`

`Platform Adapter -> OS`

Domain katmanı UI, PySide6 veya işletim sistemi adapter'larına bağımlı olmamalıdır.

