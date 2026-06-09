# DEC-001 — CPS Limitleri

## Karar

MVP için tıklama hızı CPS (clicks per second) olarak yönetilecektir.

- Minimum CPS: 1
- Maksimum CPS: 100
- Varsayılan CPS: 10

## Gerekçe

Kullanıcının teknik ayarlarla uğraşmadan anlaşılır bir hız değeri girmesi gerekir. 1-100 aralığı MVP için hem basit hem de güvenli bir başlangıç sınırıdır.

## Etkilenen Görevler

- TASK-003 — Hız Ayarı Kuralları
- TASK-004 — Sol Tıklama Motoru
- TASK-011 — MVP Manuel Doğrulama Senaryoları

## Kabul Notu

Geçersiz CPS değerleriyle otomasyon başlatılmamalıdır. Varsayılan değer 10 CPS olmalıdır.

