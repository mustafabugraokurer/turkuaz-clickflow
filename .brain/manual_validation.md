# Manual Validation

## Tooling Degisikligi

TASK-028 yalnizca PM Brain ve gelistirme araci akisini degistirdi. Urun
davranisi degismedigi icin yeni manuel kullanici testi veya smoke test
gerektirmedi.

## Durum

Manuel dogrulama sistemi PM Brain V2 ile ikiye ayrilir:

- `tests/manual/`: manuel test senaryolari ve test sonucu dokumanlari
- `tasks/user-tests/`: kullanicinin yurutmesi gereken dogrulama gorevleri

## Bekleyen Kullanici Testleri

- USER-TEST-001 - CPS Validation
- USER-TEST-002 - Hotkey Validation
- USER-TEST-003 - Platform Validation
- USER-TEST-004 - macOS Permission Validation
- USER-TEST-005 - Settings Persistence Validation
- USER-TEST-006 - Window Guard Validation
- USER-TEST-007 - Release Artifact Smoke

## Bekleyen Manuel Smoke Testler

- macOS real mouse backend smoke test
- macOS izin davranisi smoke test
- macOS F8 hotkey permission smoke test
- settings persistence smoke test
- window guard smoke test
- release artifact smoke test

## Son Manuel Bulgular

- Windows MVP smoke test Passed: `1` CPS, `10` CPS, `Start` / `Stop` ve `F8 ile durduruldu` adimlari dogrulandi.
- BUG-002 cozuldu: Windows'ta global `F8` ile durdurma calisiyor.
- TASK-021 tamamlandi.
- 2026-07-05 release review guncellendi: Windows MVP Go, macOS teknik preview.
- TASK-001 kapatildi: Windows MVP kabul cercevesi netlestirildi.
- TASK-024 tamamlandi: macOS global hotkey adapter unit test seviyesinde eklendi.
- TASK-027 tamamlandi: macOS Accessibility ve Input Monitoring izin mesajlari
  ayrildi; manuel macOS izin smoke testleri bekliyor.
- TASK-025 tamamlandi: packaging stratejisi ve release artifact smoke checklist
  eklendi; gercek artifact smoke testi bekliyor.
- TASK-026 tamamlandi: settings persistence eklendi; yeniden acilista CPS,
  hotkey, hedef pencere ve pencere koruma tercihlerinin korundugu manuel smoke
  test ile dogrulanmali.
- TASK-008 tamamlandi: pencere degisince durdurma davranisi unit test
  seviyesinde eklendi; `tests/manual/window-guard-smoke.md` bekliyor.
- 2026-07-06 QA Review tamamlandi: blocker bug bulunmadi; yeni user-testler
  USER-TEST-005, USER-TEST-006 ve USER-TEST-007 olarak acildi.

## Manual Validation Kurali

Kullanici tarafindan tamamlanacak testler gelistirici task'i gibi Done'a
tasinmaz. Kullanici sonucu bildirir; Codex sonucu ilgili user-test dosyasina
isler ve gerekiyorsa bug/task olusturur.
