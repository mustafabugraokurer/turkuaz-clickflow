# Manual Validation

## Durum

Manuel dogrulama sistemi PM Brain V2 ile ikiye ayrilir:

- `tests/manual/`: manuel test senaryolari ve test sonucu dokumanlari
- `tasks/user-tests/`: kullanicinin yurutmesi gereken dogrulama gorevleri

## Bekleyen Kullanici Testleri

- USER-TEST-001 — CPS Validation
- USER-TEST-002 — Hotkey Validation
- USER-TEST-003 — Platform Validation
- USER-TEST-004 — macOS Permission Validation

## Bekleyen Manuel Smoke Testler

- TASK-021 — Windows MVP Manuel Smoke Test
- macOS real mouse backend smoke test
- macOS izin davranisi smoke test

## Son Manuel Bulgular

- BUG-001 bulundu ve cozuldu: CPS UI refresh sirasinda 10'a donuyordu.
- macOS hata mesajlari daha net hale getirildi: izin hatasi artik teknik olmayan mesajla gosterilir.

## Manual Validation Kurali

Kullanici tarafindan tamamlanacak testler gelistirici task'i gibi Done'a
tasinmaz. Kullanici sonucu bildirir; Codex sonucu ilgili user-test dosyasina
isler ve gerekiyorsa bug/task olusturur.

## User Validation Workflow

Kullanici test sonucu bildirdiginde:

1. Sonuc beklenen davranisla karsilastirilir.
2. Sonuc Passed / Failed / Blocked olarak etiketlenir.
3. Failed ise bug mi feature gap mi oldugu belirlenir.
4. Bug ise `tasks/todo/BUG-xxx-...md` olusturulur.
5. Feature gap ise `tasks/todo/TASK-xxx-...md` olusturulur.
6. Risk ve release status dosyalari guncellenir.
