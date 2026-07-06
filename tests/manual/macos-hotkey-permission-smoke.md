# macOS Hotkey Permission Smoke Test

## Amac

macOS global `F8` kisayolunun Input Monitoring izni eksikken kullaniciya net
mesaj verdigini ve izin verildikten sonra uygulama odakta degilken de
calistigini manuel olarak dogrulamak.

## On Kosullar

- Test macOS uzerinde calistirilmalidir.
- Uygulama veya terminal icin Input Monitoring izni kontrol edilebilmelidir.
- Guvenli hedef alan hazirlanmalidir.

## Adimlar

1. macOS Sistem Ayarlari > Gizlilik ve Guvenlik > Input Monitoring icinde
   uygulama veya terminal iznini kapat.
2. Uygulamayi baslat.
3. `F8` kisayolunu dene.
4. Mesaj alaninda Input Monitoring izin ihtiyacinin belirtildigini dogrula.
5. Input Monitoring iznini ver.
6. Uygulamayi yeniden baslat.
7. Uygulamayi arka plana al.
8. `F8` ile otomasyonu baslat.
9. `F8` ile otomasyonu durdur.

## Beklenen Sonuc

- Izin yoksa kullanici su mesaji gorur:
  `macOS Input Monitoring izni gerekli olabilir. Sistem Ayarları > Gizlilik ve Güvenlik > Input Monitoring bölümünden uygulamaya izin verin.`
- Izin verildikten sonra `F8` uygulama odakta degilken de start/stop davranisini
  tetikler.
- Stop reason `F8 ile durduruldu` olarak gorunur.
