# USER-TEST-002 — Hotkey Validation

## Amaç

F8 kisa yolunun otomasyonu baslatma ve durdurma davranisini dogrulamak.

## Platform

Windows smoke testte Passed. macOS icin TASK-024 sonrasi manuel retest bekliyor.

## Adimlar

1. Uygulamayi ac.
2. F8'e bas.
3. Otomasyonun calistigini dogrula.
4. Uygulamayi arka plana al.
5. F8'e tekrar bas.
6. Otomasyonun durdugunu ve mesajda F8 ile durduruldu bilgisinin gorundugunu dogrula.

## Beklenen Sonuc

- F8 Start/Stop toggle davranisini tetikler.
- Uygulama odakta degilken de Windows ve macOS'ta calisir.
- Stop reason `HOTKEY_STOPPED` olarak gorunur.

## Durum

Bekliyor.
