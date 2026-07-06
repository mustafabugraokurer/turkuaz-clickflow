# USER-TEST-005 - Settings Persistence Validation

## Amac

CPS, hotkey, hedef pencere ve pencere koruma tercihlerinin uygulama yeniden
acildiginda korundugunu dogrulamak.

## Platform

Windows ve macOS

## Adimlar

1. Uygulamayi baslat.
2. CPS degerini `25` yap.
3. Hedef pencere sec.
4. `Pencere degisince durdur` secenegini ac.
5. Uygulamayi kapat.
6. Uygulamayi yeniden baslat.
7. CPS degerinin `25` olarak geldigini dogrula.
8. Hedef pencere seciminin veya secim basliginin korundugunu dogrula.
9. Pencere koruma seceneginin acik geldigini dogrula.
10. Config dosyasini boz veya gecersiz CPS degeri yaz.
11. Uygulamayi yeniden baslat.

## Beklenen Sonuc

- Gecerli ayarlar yeniden acilista korunur.
- Bozuk veya gecersiz config uygulamayi baslatmayi engellemez.
- Bozuk config durumunda varsayilan CPS `10` ve hotkey `F8` ile devam edilir.

## Durum

Bekliyor.
