# USER-TEST-007 - Release Artifact Smoke

## Amac

Packaging sonrasi uretilen artifact'in temiz ortamda acildigini ve MVP
davranislarini korudugunu dogrulamak.

## Platform

Windows portable zip ve macOS app bundle / dmg preview.

## Adimlar

1. Artifact'i temiz test klasorune kopyala.
2. Uygulamayi baslat.
3. Ana pencerenin acildigini dogrula.
4. Varsayilan CPS degerinin `10` oldugunu dogrula.
5. CPS degerini `1` yap.
6. Start / Stop akisini dogrula.
7. CPS degerini `10` yap ve Start / Stop akisini tekrar dene.
8. F8 ile durdurma davranisini dogrula.
9. Hedef pencere listesinin acildigini dogrula.

## Beklenen Sonuc

- Artifact beklenen platform acilis akisiyle baslar.
- Windows MVP davranislari korunur.
- macOS preview artifact izin eksiklerinde sessiz kalmaz.
- Kritik hata veya crash yoktur.

## Durum

Bekliyor.
