# USER-TEST-004 — macOS Permission Validation

## Amaç

macOS Accessibility veya Input Monitoring izinleri eksikken ve izinler
verildikten sonra uygulamanin kullaniciya net geri bildirim verdigini
dogrulamak.

## Platform

macOS

## Adimlar

1. Uygulama veya terminal icin Accessibility iznini kapat.
2. Uygulamayi baslat.
3. Start'a bas.
4. Mesaj alaninda izin ihtiyacinin net belirtildigini dogrula.
5. Accessibility iznini ver.
6. Uygulamayi tekrar baslat.
7. Start / Stop akisini tekrar dene.

## Beklenen Sonuc

- Izin yoksa uygulama sessizce calisir gibi gorunmez.
- Mesaj: `macOS erişilebilirlik izni gerekli olabilir.`
- Izin verildikten sonra tiklama dongusu guvenli hedef alanda calisir.

## Durum

Bekliyor.
