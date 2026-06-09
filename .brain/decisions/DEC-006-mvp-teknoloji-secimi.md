# DEC-006 — MVP Teknoloji Seçimi

## Karar

MVP teknolojisi Python olacaktır.

UI için PySide6 kullanılacaktır.

## Gerekçe

PySide6, Turkuaz ClickFlow'un Windows ve macOS desteği hedefiyle uyumludur. Ürün gelecekte daha profesyonel görünüme, daha karmaşık otomasyon ekranlarına ve daha uzun vadeli sürdürülebilirliğe ihtiyaç duyacaktır.

Ürünün büyüme hattı şu şekilde öngörülmektedir:

- Turkuaz ClickFlow
- Turkuaz Macro
- Turkuaz Automation

Bu büyüme olasılığı nedeniyle PySide6, CustomTkinter'a göre daha mantıklı MVP tercihidir.

## Mimari Etki

- UI katmanı PySide6 ile oluşturulacaktır.
- Ortak ürün mantığı UI katmanından bağımsız tutulacaktır.
- Mouse, klavye, global kısayol ve pencere işlemleri platform adapter katmanında ayrılacaktır.
- Windows ve macOS aynı ürün akışını ve aynı UI yapısını paylaşacaktır.

## Etkilenen Görevler

- TASK-001 — MVP Kabul Çerçevesi
- TASK-002 — Ana Yüzey Bilgi Mimarisi
- TASK-004 — Sol Tıklama Motoru
- TASK-005 — Start / Stop Durum Makinesi
- TASK-006 — Global Kısayol
- TASK-009 — Sayaç ve Çalışma Süresi
- TASK-010 — Durum, Uyarı ve Durma Sebebi Mesajları
- TASK-011 — MVP Manuel Doğrulama Senaryoları

## Kabul Notu

Sprint-1'de teknoloji kararına uygun mimari iskelet kurulmalıdır. Kod yazımına geçmeden önce PySide6 UI katmanı, platform adapter katmanı ve platformdan bağımsız uygulama/domain katmanı ayrımı görünür olmalıdır.

