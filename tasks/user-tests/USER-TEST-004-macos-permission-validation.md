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
4. Mesaj alaninda Accessibility izin ihtiyacinin net belirtildigini dogrula.
5. Accessibility iznini ver.
6. Uygulamayi tekrar baslat.
7. Input Monitoring iznini kapat.
8. F8 kısayolunu dene.
9. Mesaj alaninda Input Monitoring izin ihtiyacinin net belirtildigini dogrula.
10. Input Monitoring iznini ver.
11. Uygulamayi tekrar baslat.
12. Start / Stop ve F8 akisini tekrar dene.

## Beklenen Sonuc

- Izin yoksa uygulama sessizce calisir gibi gorunmez.
- Mouse/tiklama izin mesaji: `macOS Accessibility izni gerekli olabilir. Sistem Ayarları > Gizlilik ve Güvenlik > Accessibility bölümünden uygulamaya izin verin.`
- Hotkey izin mesaji: `macOS Input Monitoring izni gerekli olabilir. Sistem Ayarları > Gizlilik ve Güvenlik > Input Monitoring bölümünden uygulamaya izin verin.`
- Izin verildikten sonra tiklama dongusu guvenli hedef alanda calisir.
- Izin verildikten sonra F8 uygulama odakta degilken de calisir.

## Durum

Bekliyor.
