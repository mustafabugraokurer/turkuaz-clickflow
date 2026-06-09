# Windows Real Mouse Backend Smoke Test

## Amaç

Windows gerçek mouse backend'inin güvenli bir hedef alanda sol tık ürettiğini
manuel olarak doğrulamak.

## Ön Koşullar

- Test Windows üzerinde çalıştırılmalıdır.
- Güvenli bir hedef alan hazırlanmalıdır.
- Test sırasında önemli uygulama pencereleri ve veri giriş alanları kapalı olmalıdır.

## Adımlar

1. Uygulamayı Windows üzerinde başlat.
2. Güvenli hedef alanı aktif hale getir.
3. CPS değerini `1` yap.
4. Start akışı ClickRunner'a bağlandıktan sonra otomasyonu başlat.
5. Kısa süre gözlemle.
6. Stop veya F8 ile durdur.

## Beklenen Sonuç

- Gerçek sol tık üretilir.
- Sayaç yalnızca gerçekleşen tıklamalarla artar.
- Stop veya F8 sonrası yeni tıklama üretilmez.
- Hata oluşursa otomasyon güvenli şekilde durur ve kullanıcıya teknik olmayan mesaj gösterilir.

## Not

TASK-019 yalnızca gerçek Windows mouse backend'ini ekler. UI ClickRunner çalışma
döngüsü TASK-020 ile bağlanacağı için bu smoke testin tam yürütümü TASK-020
sonrasında yapılmalıdır.
