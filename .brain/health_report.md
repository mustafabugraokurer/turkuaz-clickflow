# Health Report

## Sprint

Sprint-1: Windows odakli minimum auto clicker cekirdegi ve macOS uyumluluk hazirligi.

## Health Score Calculation

Bu dosya karar motoru olarak kullanilir. Skorlar release blocker, test, platform
hazirligi ve manuel dogrulama durumuna gore guncellenir.

## Sprint Progress

88%

Gerekce:

- Cekirdek gelistirme gorevleri tamamlandi.
- Windows manuel smoke test bekleniyor.
- TASK-001 tarihsel planlama kalintisi olarak duruyor.

## Test Count

106 unit test basarili.

```bash
PYTHONPATH=src python3 -m unittest discover -s tests/unit
```

## Open Bugs

Yok.

## Open Tasks

- TASK-001 — MVP Kabul Cercevesi
- TASK-021 — Windows MVP Manuel Smoke Test
- TASK-007 — Pencere Listeleme ve Hedef Secimi
- TASK-008 — Pencere Degisince Durdurma Davranisi

## Release Readiness

78%

Karar: No-Go

Gerekce:

- Acik bug yok.
- 106 unit test basarili.
- Windows uzerinde uctan uca manuel smoke test tamamlanmadi.

## Platform Readiness

- Windows: 70%
  - Real mouse backend var.
  - Global F8 adapter var.
  - Manuel Windows smoke test bekleniyor.
- macOS: 85%
  - Real mouse backend var.
  - Global hotkey adapter yok.
  - Accessibility/Input Monitoring izin deneyimi manuel dogrulanmali.

## Suggested User Tests

- USER-TEST-001 — CPS Validation
- USER-TEST-002 — Hotkey Validation
- USER-TEST-003 — Platform Validation
- USER-TEST-004 — macOS Permission Validation

## Suggested New Tasks

- TASK-021 — Windows MVP Manuel Smoke Test
- TASK-024 — macOS Global Hotkey Adapter
- TASK-025 — Packaging Strategy
- TASK-026 — Settings Persistence
- TASK-027 — macOS Permission UX Review

## Suggested Next Action

TASK-021 — Windows MVP Manuel Smoke Test

## Decision Rationale

Release No-Go durumunun ana nedeni Windows smoke test eksigidir. Bu nedenle
devam et komutu geldiginde karar motoru once TASK-021'i secer. Mevcut ortam
Windows degilse TASK-021 blocked kalir ve siradaki mantikli aksiyon macOS
permission validation veya macOS global hotkey task'i olur.

## Release Status

No-Go.

Release icin Windows manuel smoke test sonucu beklenmektedir.
