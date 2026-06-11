# macOS Real Mouse Backend Smoke Test

## Amaç

macOS gerçek mouse backend'inin güvenli bir hedef alanda sol tık ürettiğini
manuel olarak doğrulamak.

## Ön Koşullar

- Test macOS üzerinde çalıştırılmalıdır.
- Uygulamaya gerekirse Accessibility izni verilmelidir.
- macOS sürümüne ve çalıştırma biçimine göre Input Monitoring izni gerekebilir.
- Güvenli ve boş bir hedef alan hazırlanmalıdır.
- Test sırasında önemli uygulama pencereleri ve veri giriş alanları kapalı olmalıdır.

## Adımlar

1. macOS Sistem Ayarları içinde uygulama veya terminal için Accessibility iznini kontrol et.
2. Gerekirse Input Monitoring iznini kontrol et.
3. Uygulamayı macOS üzerinde başlat.
4. Güvenli hedef alanı aktif hale getir.
5. CPS değerini `1` yap.
6. Start butonuna bas.
7. Gerçek sol tık üretimini ve sayaç artışını gözlemle.
8. Stop butonuna bas.
9. Stop sonrası yeni tıklama üretilmediğini doğrula.

## Beklenen Sonuç

- Gerçek sol tık üretilir.
- Sayaç yalnızca gerçekleşen tıklamalarla artar.
- Stop sonrası yeni tıklama üretilmez.
- İzin eksikliği varsa otomasyon sessizce çalışır gibi görünmez; hata güvenli şekilde yüzeye çıkar.

## Not

macOS global hotkey implementasyonu bu task kapsamında değildir.
