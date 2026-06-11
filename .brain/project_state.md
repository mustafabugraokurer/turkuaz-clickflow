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

- BUG-001 — CPS UI Reset
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
- TASK-022 — macOS Real Mouse Backend

## Devam Eden / Kalan Sprint-1 Gorevleri

- TASK-001 — MVP Kabul Cercevesi
- TASK-021 — Windows MVP Manuel Smoke Test

## Açık Buglar

Yok.

## Çözülen Buglar

- BUG-001 — CPS degeri UI'da 10'a geri donuyordu. ViewModel secili CPS degerini koruyacak sekilde guncellendi.

## MVP Kapanis Durumu

MVP kabul edilmedi; revizyon gereklidir. TASK-012 kapsam kapanis kontrolu, Windows uctan uca manuel smoke test eksik oldugu icin MVP'nin henuz ilk kullanilabilir auto clicker olarak kapanamayacagini kaydetmistir.

TASK-021 mevcut `darwin` ortaminda calistirilamaz. Windows manuel smoke test sonucu beklenmektedir.

BUG-001 cozuldu. MVP release karari icin Windows manuel smoke test sonucu beklenmektedir.

PM Brain V2 aktif hale getirildi. Product Owner, QA ve Release Agent rolleri
AGENTS.md icinde tanimlandi. Health, risk, manual validation ve release status
dosyalari olusturuldu.

Tamamlanan temel gelistirici gorevleri:

- TASK-013 — PySide6 Ana Pencere MVP
- TASK-014 — Platform Adapter Interface
- TASK-015 — Mouse Click Adapter
- TASK-016 — Click Runner
- TASK-017 — UI ile AutomationService Baglantisi
- TASK-018 — OS Global Hotkey Adapter
- TASK-019 — Windows Real Mouse Backend
- TASK-020 — UI ClickRunner Calisma Dongusu Baglantisi
- TASK-022 — macOS Real Mouse Backend

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

Sonuc: 106 test basarili.

## Sonraki Onerilen Task

TASK-021 — Windows MVP Manuel Smoke Test.

## PM Brain V2 Dosyalari

- `.brain/health_report.md`
- `.brain/open_risks.md`
- `.brain/manual_validation.md`
- `.brain/release_status.md`
- `tasks/user-tests/`
- `reviews/product-review-2026-06-11.md`
