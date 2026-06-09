# DEC-005 — Platform Desteği ve Adapter Kararı

## Karar

Turkuaz ClickFlow hem Windows hem macOS destekleyecek şekilde tasarlanacaktır.

MVP hedefi:

- Windows desteği
- macOS için temel uyumluluk hazırlığı

## Gerekçe

İlk geliştirme Windows odaklı yapılabilir; ancak macOS desteği mimaride baştan düşünülmelidir. Mouse, klavye ve pencere işlemleri işletim sistemine göre farklı uygulanacağı için platforma özel işlemler adapter yapısıyla ayrılmalıdır.

Windows ve macOS aynı arayüzü kullanacak; ortak ürün mantığı platformdan bağımsız kalacaktır.

## Mimari Kural

Platforma özel işlemler adapter yapısına ayrılmalıdır:

- Windows adapter
- macOS adapter

Platformdan bağımsız kalması gereken alanlar:

- Ortak ürün mantığı
- Sayaç
- Durum makinesi
- UI

İşletim sistemine göre ayrı uygulanacak alanlar:

- Pencere listeleme
- Global kısayol
- Otomatik tıklama
- Mouse ve klavye işlemleri

## Etkilenen Görevler

- TASK-001 — MVP Kabul Çerçevesi
- TASK-004 — Sol Tıklama Motoru
- TASK-006 — Global Kısayol
- TASK-007 — Pencere Listeleme ve Hedef Seçimi
- TASK-008 — Pencere Değişince Durdurma Davranışı
- TASK-011 — MVP Manuel Doğrulama Senaryoları

## Kabul Notu

Sprint-1 geliştirmesi Windows odaklı ilerleyebilir. Ancak mouse, klavye, global kısayol ve pencere işlemleri platform adapter sınırları düşünülerek planlanmalıdır. Bu karar teknoloji seçimi değildir; hedef platform ve mimari ayrım kararıdır.
