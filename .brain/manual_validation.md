# Manual Validation

## Durum

Manuel dogrulama sistemi PM Brain V2 ile ikiye ayrilir:

- `tests/manual/`: manuel test senaryolari ve test sonucu dokumanlari
- `tasks/user-tests/`: kullanicinin yurutmesi gereken dogrulama gorevleri

## Bekleyen Kullanici Testleri

- USER-TEST-001 - CPS Validation
- USER-TEST-002 - Hotkey Validation
- USER-TEST-003 - Platform Validation
- USER-TEST-004 - macOS Permission Validation

## Bekleyen Manuel Smoke Testler

- macOS real mouse backend smoke test
- macOS izin davranisi smoke test

## Son Manuel Bulgular

- Windows MVP smoke test Passed: `1` CPS, `10` CPS, `Start` / `Stop` ve `F8 ile durduruldu` adimlari dogrulandi.
- BUG-002 cozuldu: Windows'ta global `F8` ile durdurma calisiyor.
- TASK-021 tamamlandi.

## Manual Validation Kurali

Kullanici tarafindan tamamlanacak testler gelistirici task'i gibi Done'a
tasinmaz. Kullanici sonucu bildirir; Codex sonucu ilgili user-test dosyasina
isler ve gerekiyorsa bug/task olusturur.
