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

- BUG-001 - CPS UI Reset
- BUG-002 - Windows F8 ile durdurma calismiyor
- TASK-002 - Ana Yuzey Bilgi Mimarisi
- TASK-003 - Hiz Ayari Kurallari
- TASK-004 - Sol Tiklama Motoru, domain temeli kismi tamamlandi
- TASK-005 - Start / Stop Durum Makinesi
- TASK-006 - Global Kisayol Baslat / Durdur Akisi
- TASK-007 - Pencere Listeleme ve Hedef Secimi
- TASK-009 - Sayac ve Calisma Suresi
- TASK-010 - Durum, Uyari ve Durma Sebebi Mesajlari
- TASK-011 - MVP Manuel Dogrulama Senaryolari
- TASK-012 - MVP Kapsam Kapanis Kontrolu
- TASK-013 - PySide6 Ana Pencere MVP
- TASK-014 - Platform Adapter Interface
- TASK-015 - Mouse Click Adapter
- TASK-016 - Click Runner
- TASK-017 - UI ile AutomationService Baglantisi
- TASK-018 - OS Global Hotkey Adapter
- TASK-019 - Windows Real Mouse Backend
- TASK-020 - UI ClickRunner Calisma Dongusu Baglantisi
- TASK-021 - Windows MVP Manuel Smoke Test
- TASK-022 - macOS Real Mouse Backend

## Devam Eden / Kalan Sprint-1 Gorevleri

- TASK-001 - MVP Kabul Cercevesi

## Acik Buglar

Yok.

## Cozulen Buglar

- BUG-001 - CPS degeri UI'da 10'a geri donuyordu.
- BUG-002 - Windows global `F8` ile durdurma calismiyordu; retest ile dogrulandi.

## MVP Kapanis Durumu

Windows MVP kabul kriterleri kullanici smoke testi ile saglandi. `Start` / `Stop`,
`1` CPS, `10` CPS ve global `F8` durdurma akisi dogrulandi.

Windows icin ana release blocker kapandi. macOS tarafi teknik preview seviyesinde
olmaya devam ediyor.

## Sprint-1 Disi / Opsiyonel

- TASK-008 - Pencere Degisince Durdurma Davranisi

## Son Dogrulama

Son unit test sonucu:

```bash
PYTHONPATH=src python -m unittest discover -s tests/unit
```

Sonuc: 118 test basarili.

## Sonraki Onerilen Task

RELEASE REVIEW
