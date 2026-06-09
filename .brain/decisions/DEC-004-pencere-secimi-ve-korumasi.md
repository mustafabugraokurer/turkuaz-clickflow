# DEC-004 — Pencere Seçimi ve Koruması

## Karar

MVP'de pencere seçimi isteğe bağlı olacaktır. Pencere koruması da opsiyonel olacaktır.

## Gerekçe

Ürün ilk sürümde basit auto clicker davranışını hızlıca sunmalıdır. Pencere hedefleme güvenlik ve kontrol için desteklenecek, ancak kullanıcıyı başlatma öncesi zorunlu bir seçimle durdurmayacaktır.

## Etkilenen Görevler

- TASK-007 — Pencere Listeleme ve Hedef Seçimi
- TASK-008 — Pencere Değişince Durdurma Davranışı
- TASK-010 — Durum, Uyarı ve Durma Sebebi Mesajları
- TASK-011 — MVP Manuel Doğrulama Senaryoları

## Kabul Notu

Hedef pencere seçilmeden otomasyon başlatılabilir. Pencere koruması açıkken hedef pencere değişirse veya kapanırsa otomasyon durmalıdır.

