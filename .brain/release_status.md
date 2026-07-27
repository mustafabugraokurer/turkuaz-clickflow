# Release Status

## Current Recommendation

Go

## Release Readiness Score

96%

## Neden

Windows uzerinde uctan uca manuel smoke test Passed sonuc verdi ve BUG-002
kapatildi. Ana release blockerlar kalmadi.

TASK-028 ile yapilan Codebase Memory MCP entegrasyonu yalnizca gelistirme ve
analiz akisini etkiler; urun davranisini, artifact'i veya mevcut Go kararini
degistirmez.

## Go Icin Minimum Kosullar

- Start / Stop / F8 / CPS / sayac / sure Windows ortaminda dogrulanmali. Passed
- Kritik release blocker bug kalmamali. Passed

## Platform Durumu

### Windows

Durum: Windows MVP icin release candidate hazir.

Readiness: 92%

Hazir olanlar:

- Real mouse backend
- UI ClickRunner dongusu
- F8 global hotkey adapter
- CPS UI reset bug fix
- Hedef pencere listeleme ve secimi
- Pencere degisince durdurma davranisi
- Settings persistence
- `Start` / `Stop`, `1` CPS, `10` CPS ve `F8` manuel olarak dogrulandi

Eksik:

- Packaging artifact uretimi ve smoke test

### macOS

Durum: Teknik preview seviyesinde.

Readiness: 93%

Hazir olanlar:

- Real mouse backend
- UI ClickRunner dongusu
- Izin hatasi icin daha net mesaj
- Global hotkey adapter
- Accessibility/Input Monitoring izin mesajlari ayrildi
- Settings persistence

Eksik:

- macOS global hotkey manuel smoke test
- macOS izin deneyimi dogrulamasi
- macOS release packaging / signing / notarization

## Open Release Blockers

Yok.

## Decision Engine Next Action

USER-TEST-006 - Window Guard Validation

Gerekce:

- High severity Windows blocker kapandi.
- Kullanici smoke testi Passed sonuc verdi.
- 2026-07-05 release review guncellendi.
- TASK-001 kapatildi.
- TASK-024 tamamlandi.
- TASK-027 tamamlandi.
- TASK-025 tamamlandi.
- TASK-026 tamamlandi.
- TASK-008 tamamlandi.
- QA Review tamamlandi.
- Siradaki mantikli aksiyon window guard manuel smoke testidir.

## Recently Resolved

- BUG-001 - CPS UI Reset
- BUG-002 - Windows F8 ile durdurma calismiyor
- TASK-001 - MVP Kabul Cercevesini Netlestir
- TASK-024 - macOS Global Hotkey Adapter
- TASK-025 - Packaging Strategy
- TASK-026 - Settings Persistence
- TASK-027 - macOS Permission UX Review
- TASK-008 - Pencere Degisince Durdurma Davranisi
- TASK-028 - Codebase Memory MCP PM Brain Entegrasyonu
