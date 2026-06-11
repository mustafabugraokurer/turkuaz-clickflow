# USER-TEST-001 — CPS Validation

## Amaç

Kullanicinin sectigi CPS degerinin UI refresh, Start ve Stop sonrasinda
korundugunu dogrulamak.

## Platform

Windows ve macOS

## Adimlar

1. Uygulamayi ac.
2. CPS degerini `1` yap.
3. 3 saniye bekle.
4. CPS alaninin `1` kaldigini dogrula.
5. Start'a bas.
6. Stop'a bas.
7. CPS alaninin hala `1` oldugunu dogrula.
8. CPS degerini `25` yap ve ayni akisi tekrarla.

## Beklenen Sonuc

- CPS degeri `10` degerine geri donmez.
- Start secilen CPS ile calisir.
- Stop sonrasi secilen CPS korunur.

## Durum

Bekliyor.
