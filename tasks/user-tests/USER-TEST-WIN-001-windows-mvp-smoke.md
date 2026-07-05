# USER-TEST-WIN-001 - Windows MVP Smoke Validation

## Durum

Passed.

## Bagli Gorev

- TASK-021 - Windows MVP Manuel Smoke Test

## Amac

Windows ortaminda MVP'nin gercek UI, gercek mouse tiklama ve global `F8`
kisayolu ile uctan uca dogrulanmasi.

## Test Adimlari

1. Uygulamayi Windows ortaminda baslat.
2. Guvenli ve bos bir hedef alan ac.
3. CPS degerini `1` yap.
4. `Start` ile otomasyonu baslat.
5. Gercek sol tik uretimini ve sayac artislarini gozlemle.
6. `Stop` ile otomasyonu durdur ve yeni tiklama uremedigini dogrula.
7. CPS degerini `10` yap.
8. `F8` ile otomasyonu baslat.
9. Uygulamayi arka plana al.
10. `F8` ile otomasyonu durdur.
11. Durma sebebinin `F8 ile durduruldu` olarak gosterildigini dogrula.

## Beklenen Sonuc

- Uygulama Windows'ta acilir.
- Start gercek tiklama uretir.
- Stop ve F8 guvenli sekilde durdurur.
- Sayac yalnizca gerceklesen tiklamalarla artar.
- Kritik bloklayici hata kalmaz.

## Son Test Sonucu

- Tarih: 2026-07-05
- Platform: Windows
- Test sonucu: Passed
- Bulgular:
  - `1` CPS tiklama calisti.
  - `Start` ve `Stop` butonlari calisti.
  - `10` CPS tiklama calisti.
  - `F8 ile durduruldu` davranisi son retest'te calisti.
- Acilan bug veya task:
  - BUG-002 acildi ve cozuldu.
