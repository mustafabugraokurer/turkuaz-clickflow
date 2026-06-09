# DEC-003 — Yeni Çalıştırmada Sayaç Sıfırlama

## Karar

Her yeni otomasyon çalıştırmasında tıklama sayacı sıfırlanacaktır.

## Gerekçe

MVP'de kullanıcının son çalıştırmanın sonucunu kolayca anlaması önceliklidir. Oturumlar arası kalıcı sayaç veya geçmiş V2+ kapsamına bırakılmıştır.

## Etkilenen Görevler

- TASK-009 — Sayaç ve Çalışma Süresi
- TASK-010 — Durum, Uyarı ve Durma Sebebi Mesajları
- TASK-011 — MVP Manuel Doğrulama Senaryoları

## Kabul Notu

Start verildiğinde sayaç 0'dan başlamalıdır. Stop sonrası son değer kullanıcıya görünür kalmalıdır.

