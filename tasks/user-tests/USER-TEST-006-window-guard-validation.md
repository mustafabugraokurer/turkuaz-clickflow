# USER-TEST-006 - Window Guard Validation

## Amac

`Pencere degisince durdur` secenegi acikken otomasyonun hedef pencere disinda
tiklama yapmadan durdugunu dogrulamak.

## Platform

Windows. macOS pencere sorgulama adapter'i tamamlandiginda macOS icin de
calistirilir.

## Adimlar

1. Uygulamayi baslat.
2. Hedef pencere listesinden guvenli bir hedef pencere sec.
3. `Pencere degisince durdur` secenegini ac.
4. CPS degerini `1` yap.
5. Start'a bas.
6. Hedef pencere aktifken tiklama ve sayac artisinin calistigini dogrula.
7. Baska bir pencereye gec.
8. Otomasyonun durdugunu dogrula.
9. Mesajda `Pencere degisti` bilgisinin gorundugunu dogrula.
10. Hedef pencereyi kapatip ayni akisi tekrar dene.

## Beklenen Sonuc

- Hedef pencere aktifken otomasyon calisir.
- Aktif pencere degisirse yeni tiklama gonderilmeden otomasyon durur.
- Hedef pencere kapanirsa otomasyon durur.
- Stop ve F8 ile durdurma davranislari normal sekilde calismaya devam eder.

## Durum

Bekliyor.
