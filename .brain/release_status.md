# Release Status

## Current Recommendation

No-Go

## Release Readiness Score

78%

## Neden

Windows uzerinde uctan uca manuel smoke test tamamlanmamistir.

## Go Icin Minimum Kosullar

- TASK-021 Windows MVP Manuel Smoke Test tamamlanmali.
- Start / Stop / F8 / CPS / sayac / sure Windows ortaminda dogrulanmali.
- Kritik release blocker bug kalmamali.

## Platform Durumu

### Windows

Durum: Release candidate'a yakin, manuel smoke test bekliyor.

Readiness: 70%

Hazir olanlar:

- Real mouse backend
- UI ClickRunner dongusu
- F8 global hotkey adapter
- CPS UI reset bug fix

Eksik:

- Windows manuel smoke test sonucu

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

- TASK-021 — Windows MVP Manuel Smoke Test

## Decision Engine Next Action

TASK-021 — Windows MVP Manuel Smoke Test

Gerekce:

- High severity risk: Windows smoke test eksik.
- Acik bug yok.
- Release No-Go sebebi Windows manuel dogrulama eksigi.

## Recently Resolved

- BUG-001 — CPS UI Reset
