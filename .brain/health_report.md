# Health Report

## Sprint

Sprint-1: Windows odakli minimum auto clicker cekirdegi ve macOS uyumluluk hazirligi.

## Sprint Progress

97%

Gerekce:

- Cekirdek gelistirme gorevleri tamamlandi.
- Windows MVP smoke testi Passed sonuc verdi.
- Eski release blocker olan BUG-002 kapatildi.
- TASK-001 tarihsel planlama kalintisi olarak duruyor.

## Test Count

118 unit test basarili.

```bash
PYTHONPATH=src python -m unittest discover -s tests/unit
```

## Open Bugs

Yok.

## Open Tasks

- TASK-001 - MVP Kabul Cercevesi
- TASK-008 - Pencere Degisince Durdurma Davranisi

## Release Readiness

90%

Karar: Go

Gerekce:

- Acik release blocker bug yok.
- 118 unit test basarili.
- Windows uzerinde uctan uca manuel smoke test Passed sonuc verdi.

## Platform Readiness

- Windows: 92%
- Real mouse backend var.
- Global F8 hotkey akisi manuel olarak dogrulandi.
- `Start` / `Stop`, `1` CPS ve `10` CPS manuel olarak dogrulandi.
- Hedef pencere listeleme ve secimi var.
- macOS: 85%
- Real mouse backend var.
- Global hotkey adapter yok.
- Accessibility/Input Monitoring izin deneyimi manuel dogrulanmali.

## Suggested User Tests

- USER-TEST-001 - CPS Validation
- USER-TEST-002 - Hotkey Validation
- USER-TEST-003 - Platform Validation
- USER-TEST-004 - macOS Permission Validation

## Suggested New Tasks

- TASK-008 - Pencere Degisince Durdurma Davranisi
- TASK-024 - macOS Global Hotkey Adapter
- TASK-025 - Packaging Strategy
- TASK-026 - Settings Persistence
- TASK-027 - macOS Permission UX Review

## Suggested Next Action

RELEASE REVIEW

## Decision Rationale

Windows MVP icin ana release blockerlar kapandi. Bu nedenle en mantikli sonraki
aksiyon yeni bir bug degil, release gozden gecirmesidir.
