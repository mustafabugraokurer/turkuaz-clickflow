# Project State

## Urun

Turkuaz ClickFlow, tekrar eden masaustu tiklama islemlerini guvenli ve kontrollu sekilde otomatiklestiren masaustu otomasyon uygulamasidir.

## Aktif Sprint

Sprint-1: Windows odakli minimum auto clicker cekirdegi ve macOS uyumluluk hazirligi.

## Gecerli Kararlar

- CPS araligi: minimum 1, maksimum 100, varsayilan 10.
- Varsayilan global kisayol: F8.
- Yeni calistirmada sayac sifirlanir.
- Pencere secimi istege baglidir.
- Pencere korumasi opsiyoneldir.
- Urun Windows ve macOS destekleyecek sekilde tasarlanir.
- MVP teknolojisi Python, UI PySide6.
- Platforma ozel mouse, klavye, pencere ve kisayol islemleri adapter yapisina ayrilir.

## Tamamlanan Sprint-1 Gorevleri

- TASK-002 — Ana Yuzey Bilgi Mimarisi
- TASK-003 — Hiz Ayari Kurallari
- TASK-004 — Sol Tiklama Motoru, domain temeli kismi tamamlandi
- TASK-005 — Start / Stop Durum Makinesi
- TASK-006 — Global Kisayol Baslat / Durdur Akisi
- TASK-009 — Sayac ve Calisma Suresi
- TASK-010 — Durum, Uyari ve Durma Sebebi Mesajlari
- TASK-011 — MVP Manuel Dogrulama Senaryolari
- TASK-012 — MVP Kapsam Kapanis Kontrolu
- TASK-013 — PySide6 Ana Pencere MVP
- TASK-014 — Platform Adapter Interface
- TASK-015 — Mouse Click Adapter
- TASK-016 — Click Runner
- TASK-017 — UI ile AutomationService Baglantisi
- TASK-018 — OS Global Hotkey Adapter
- TASK-019 — Windows Real Mouse Backend
- TASK-020 — UI ClickRunner Calisma Dongusu Baglantisi

## Devam Eden / Kalan Sprint-1 Gorevleri

- TASK-001 — MVP Kabul Cercevesi
- TASK-021 — Windows MVP Manuel Smoke Test

## MVP Kapanis Durumu

MVP kabul edilmedi; revizyon gereklidir. TASK-012 kapsam kapanis kontrolu, Windows uctan uca manuel smoke test eksik oldugu icin MVP'nin henuz ilk kullanilabilir auto clicker olarak kapanamayacagini kaydetmistir.

Tamamlanan temel gelistirici gorevleri:

- TASK-013 — PySide6 Ana Pencere MVP
- TASK-014 — Platform Adapter Interface
- TASK-015 — Mouse Click Adapter
- TASK-016 — Click Runner
- TASK-017 — UI ile AutomationService Baglantisi
- TASK-018 — OS Global Hotkey Adapter
- TASK-019 — Windows Real Mouse Backend
- TASK-020 — UI ClickRunner Calisma Dongusu Baglantisi

Yeni bloklayici revizyon gorevleri:

- TASK-021 — Windows MVP Manuel Smoke Test

## Sprint-1 Disi / Opsiyonel

- TASK-007 — Pencere Listeleme ve Hedef Secimi
- TASK-008 — Pencere Degisince Durdurma Davranisi

## Son Dogrulama

Son unit test sonucu:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests/unit
```

Sonuc: 92 test basarili.

## Sonraki Onerilen Task

TASK-021 — Windows MVP Manuel Smoke Test.
