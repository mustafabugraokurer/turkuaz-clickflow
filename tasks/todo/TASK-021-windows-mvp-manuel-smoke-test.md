# TASK-021 — Windows MVP Manuel Smoke Test

## Epic

EPIC-06 — MVP Kalite ve Kabul

## Amaç

Windows üzerinde MVP'nin gerçek UI, gerçek mouse tıklama ve OS global F8
kısayolu ile uçtan uca çalıştığını manuel olarak doğrulamak.

## Geliştirici Görevleri

- Windows ortamında uygulamayı başlat.
- Start / Stop buton akışını doğrula.
- F8 global kısayolunu uygulama odakta değilken doğrula.
- 1 CPS ve 10 CPS davranışını güvenli hedef alanda doğrula.
- Stop sonrası tıklamanın kesildiğini doğrula.
- Manuel test sonucunu `tests/manual/` altına yaz.

## Kabul Kriterleri

- Uygulama Windows'ta açılır.
- Start gerçek tıklama üretir.
- Stop ve F8 güvenli şekilde durdurur.
- Sayaç yalnızca gerçekleşen tıklamalarla artar.
- Kritik bloklayıcı hata kalmaz.

## Bağımlılıklar

- TASK-019
- TASK-020

## Kapsam Dışı

- macOS manuel kabul
- Pencere koruması
- Paketleme / installer

## Önerilen Sıra

21
