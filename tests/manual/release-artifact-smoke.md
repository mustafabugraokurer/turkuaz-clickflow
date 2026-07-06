# Release Artifact Smoke Test

## Amac

Packaging sonrasi uretilen artifact'in temiz ortamda acildigini ve MVP
davranislarini korudugunu dogrulamak.

## Platformlar

- Windows portable zip
- macOS app bundle / dmg preview

## On Kosullar

- Unit testler basarili olmalidir.
- Artifact temiz build sonucunda uretilmelidir.
- Test, mumkunse temiz makine veya temiz kullanici profilinde yapilmalidir.

## Ortak Adimlar

1. Artifact'i indir veya temiz test klasorune kopyala.
2. Uygulamayi baslat.
3. Ana pencerenin acildigini dogrula.
4. Varsayilan CPS degerinin `10` oldugunu dogrula.
5. CPS degerini `1` yap.
6. Start'a bas.
7. Gercek tiklama ve sayac artisinin oldugunu dogrula.
8. Stop'a bas.
9. Stop sonrasi yeni tiklama uremedigini dogrula.
10. CPS degerini `10` yap ve Start / Stop akisini tekrar dene.
11. F8 ile durdurma davranisini dogrula.
12. Hedef pencere listesinin acildigini dogrula.

## Windows Ek Adimlari

1. Uygulamayi arka plana al.
2. F8 ile otomasyonu durdur.
3. `F8 ile durduruldu` mesajini dogrula.

## macOS Ek Adimlari

1. Accessibility izni kapaliyken Start'a bas.
2. Accessibility izin mesajini dogrula.
3. Input Monitoring izni kapaliyken F8'i dene.
4. Input Monitoring izin mesajini dogrula.
5. Izinleri verip uygulamayi tekrar baslat.
6. Start / Stop ve F8 akisini tekrar dogrula.

## Beklenen Sonuc

- Artifact kurulum gerektirmeden veya platformun beklenen acilis akisiyle
  baslar.
- Windows MVP davranislari korunur.
- macOS preview artifact izin eksiklerinde sessiz kalmaz.
- Kritik hata veya crash yoktur.

## Durum

Bekliyor.
