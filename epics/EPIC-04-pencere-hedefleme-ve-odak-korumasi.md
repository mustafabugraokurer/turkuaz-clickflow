# EPIC-04 — Pencere Hedefleme ve Odak Koruması

## Amaç

Otomasyonun kullanıcının seçtiği pencere bağlamında çalışmasını ve pencere değiştiğinde güvenli şekilde durmasını sağlamak.

## MVP Kapsamı

- Aktif pencerelerin listelenmesi
- Hedef pencere seçimi
- Seçili hedef pencerenin ekranda gösterilmesi
- "Pencere değişince durdur" seçeneği
- Otomasyon çalışırken aktif pencere kontrolü
- Hedef pencere kaybolursa veya odak dışına çıkarsa güvenli durdurma

## Kapsam Dışı

- Pencere içi element seçimi
- Çoklu pencere otomasyonu
- Arka planda görünmeyen pencereye otomasyon
- Görüntü tanıma ile hedef bulma

## Kabul Kriterleri

- Kullanıcı otomasyon başlamadan hedef pencere seçebilir.
- Seçilen hedef pencere kullanıcıya okunabilir şekilde gösterilir.
- Odak koruması açıksa başka pencereye geçildiğinde otomasyon durur.
- Hedef pencere kapanırsa otomasyon durur ve durma sebebi gösterilir.
- Hedef pencere dışında tıklama yapılması MVP güvenlik kurallarına aykırı kabul edilir.

## Bağımlılıklar

- EPIC-03 Güvenli Başlatma / Durdurma ve Kısayol
- EPIC-05 Sayaç, Süre ve Durma Sebebi

