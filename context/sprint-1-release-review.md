# TASK-023 - Sprint-1 Release Review

## Durum

Tamamlandi.

## Tarih

2026-07-05

## Karar Ozeti

Sprint-1, Windows MVP release candidate olarak Go durumundadir.

Windows tarafinda `Start` / `Stop`, `1` CPS, `10` CPS ve global `F8` ile
durdurma akisi manuel smoke test ile Passed sonuc vermistir. BUG-001 ve BUG-002
kapatilmistir. Unit test paketi 146 test ile basarilidir.

macOS tarafi teknik preview seviyesindedir. Real mouse backend vardir; ancak
global hotkey ve izin deneyimi gercek macOS ortaminda manuel dogrulanmalidir.
Packaging/signing calismalari Sprint-2 kapsaminda ele alinmalidir.

## Tamamlanan Gorevler

- BUG-001 - CPS UI Reset
- BUG-002 - Windows F8 ile durdurma calismiyor
- TASK-001 - MVP Kabul Cercevesini Netlestir
- TASK-002 - Ana Yuzey Bilgi Mimarisi
- TASK-003 - Hiz Ayari Kurallari
- TASK-004 - Sol Tiklama Motoru, domain temeli kismi tamamlandi
- TASK-005 - Start / Stop Durum Makinesi
- TASK-006 - Global Kisayol Baslat / Durdur Akisi
- TASK-007 - Pencere Listeleme ve Hedef Secimi
- TASK-008 - Pencere Degisince Durdurma Davranisi
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
- TASK-024 - macOS Global Hotkey Adapter
- TASK-025 - Packaging Strategy
- TASK-026 - Settings Persistence
- TASK-027 - macOS Permission UX Review

## Kalan Gorevler

### Sprint-1 Kalintisi

Yok. TASK-001 kapatildi ve kabul kararinin dokuman izi guncellendi.

### Sprint-1 Disi / Opsiyonel

Yok. TASK-008 tamamlandi; gercek OS window guard smoke test bekliyor.

## QA Review

- Unit test durumu: 146 test basarili.
- Manuel Windows MVP smoke test: Passed.
- Bekleyen user-testler: CPS validation, hotkey validation, platform validation,
  macOS permission validation.
- Eksik manuel dogrulama: macOS real mouse backend, macOS F8 ve macOS izin
  smoke testleri.

## Product Review

Windows MVP kullanici icin temel vaadi karsilar:

- Tıklama baslatma/durdurma calisir.
- F8 ile hizli durdurma calisir.
- CPS ayari 1 ve 10 CPS senaryolarinda dogrulanmistir.
- Pencere secimi vardir.
- Sayac ve sure bilgisi gorunur.

Urunlesme icin kalan ana bosluklar:

- Packaging stratejisi var; artifact uretimi ve smoke test bekliyor.
- Ayarlar kalici hale getirildi; yeniden acilis manuel smoke testi bekliyor.
- macOS izin ve global hotkey manuel dogrulamasi tamam degil.
- Pencere degisince durdurma davranisi baglandi; manuel smoke test bekliyor.

## Release Review

### Windows

Karar: Go

Gerekce:

- Acik blocker bug yok.
- Windows smoke test Passed.
- Global F8 durdurma dogrulandi.
- Unit test paketi basarili.

### macOS

Karar: Teknik preview

Gerekce:

- Real mouse backend var.
- Global hotkey adapter unit test seviyesinde var.
- Accessibility/Input Monitoring izin mesajlari ayrildi; manuel dogrulama bekliyor.
- macOS artifact uretimi, signing ve notarization hazir degil.

## Riskler

- RISK-002 - macOS Global Hotkey Manuel Dogrulama Bekliyor: Low.
- RISK-003 - macOS Izin Deneyimi Manuel Dogrulama Bekliyor: Low.
- RISK-004 - Packaging Artifact / Installer Yok: Low.
- RISK-005 - Ayarlar Kalici Degil: Kapandi.

## Sprint-2 Onerileri

### P1

1. QA Review.
2. Window guard smoke test.
3. Settings persistence smoke test.

### P2

1. Release artifact smoke test.

## Test Sonucu

```bash
PYTHONPATH=src python3 -m unittest discover -s tests/unit
```

Son kayitli sonuc: 146 test basarili.

## Release Tavsiyesi

Windows MVP icin Go. Cross-platform public release icin No-Go.

Siradaki en mantikli aksiyon QA Review'dur.
