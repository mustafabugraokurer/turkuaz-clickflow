# Release Status

## Current Recommendation

Go

## Release Readiness Score

90%

## Neden

Windows uzerinde uctan uca manuel smoke test Passed sonuc verdi ve BUG-002
kapatildi. Ana release blockerlar kalmadi.

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
- `Start` / `Stop`, `1` CPS, `10` CPS ve `F8` manuel olarak dogrulandi

Eksik:

- Packaging / installer

### macOS

Durum: Teknik preview seviyesinde.

Readiness: 85%

Hazir olanlar:

- Real mouse backend
- UI ClickRunner dongusu
- Izin hatasi icin daha net mesaj

Eksik:

- macOS global hotkey adapter
- macOS izin deneyimi dogrulamasi
- macOS release packaging / signing / notarization

## Open Release Blockers

Yok.

## Decision Engine Next Action

RELEASE REVIEW

Gerekce:

- High severity Windows blocker kapandi.
- Kullanici smoke testi Passed sonuc verdi.
- Siradaki mantikli aksiyon release gozden gecirmesidir.

## Recently Resolved

- BUG-001 - CPS UI Reset
- BUG-002 - Windows F8 ile durdurma calismiyor
