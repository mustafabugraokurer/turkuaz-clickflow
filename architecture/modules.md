# Modüller

## `turkuaz_clickflow.ui`

PySide6 tabanlı arayüz katmanıdır.

Alt modüller:

- `views` — Ana pencere ve görsel ekran yapıları
- `viewmodels` — UI ile uygulama katmanı arasındaki durum ve komut bağları

Sprint-1 sorumlulukları:

- Start / Stop kontrol alanı
- CPS giriş alanı
- Kısayol gösterimi
- Sayaç, süre ve durum göstergeleri
- Uyarı ve durma sebebi gösterimi

## `turkuaz_clickflow.app`

Uygulama orkestrasyon katmanıdır.

Planlanan modüller:

- `automation_service` — Start / Stop akışını yönetir
- `click_runner` — Tıklama döngüsünü platform adapter ile koordine eder
- `hotkey_service` — Global kısayol olaylarını uygulama komutlarına çevirir
- `timer_service` — Çalışma süresi akışını yönetir

## `turkuaz_clickflow.domain`

Platformdan bağımsız ürün kurallarıdır.

Planlanan modüller:

- `automation_state` — Hazır, çalışıyor, durduruluyor, durdu, hata durumları
- `automation_settings` — CPS, kısayol ve çalışma ayarları
- `cps_policy` — 1-100 CPS doğrulaması ve 10 CPS varsayılanı
- `counter` — Yeni çalıştırmada sıfırlanan tıklama sayacı
- `stop_reason` — Stop, F8, geçersiz ayar, hata ve pencere değişimi durma sebepleri

## `turkuaz_clickflow.platform`

İşletim sistemi bağımlı işlemleri soyutlar.

Planlanan ortak adapter sözleşmeleri:

- Mouse tıklama adapter'ı
- Global kısayol adapter'ı
- Pencere adapter'ı
- Platform algılama / adapter seçimi

Platform implementasyonları:

- `platform/windows` — Windows tıklama, kısayol ve pencere işlemleri
- `platform/macos` — macOS tıklama, kısayol ve pencere işlemleri için hazırlık

## `turkuaz_clickflow.config`

Ürün sabitleri ve varsayılan ayarları tutar.

Sprint-1 değerleri:

- Minimum CPS: 1
- Maksimum CPS: 100
- Varsayılan CPS: 10
- Varsayılan kısayol: F8

