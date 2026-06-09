# EPIC-01 — Uygulama Kontrol Yüzeyi

## Amaç

Kullanıcının otomasyonu teknik bilgi gerektirmeden başlatıp durdurabileceği, temel ayarları görebileceği ve ürünün mevcut durumunu anlayabileceği MVP ana yüzeyini tanımlamak.

## MVP Kapsamı

- Start / Stop kontrolü
- Otomasyon durumu: hazır, çalışıyor, durdu, hata
- Tıklama hızı ayarı için alan
- Hedef pencere seçimi için alan
- Global kısayol ayarı için alan
- Toplam tıklama sayacı ve çalışma süresi göstergesi
- Basit hata ve uyarı mesajları

## Kapsam Dışı

- Çok adımlı senaryo tasarımı
- Profil yönetimi
- Makro kayıt ekranları
- OCR veya görüntü tanıma ayarları
- Kurumsal yönetim ekranları

## Kabul Kriterleri

- Kullanıcı tek ekrandan MVP ayarlarını görebilir.
- Start kontrolü yalnızca gerekli minimum ayarlar geçerliyse kullanılabilir olur.
- Stop kontrolü otomasyon çalışırken her zaman erişilebilir olur.
- Durum göstergesi otomasyonun ne yaptığını açık şekilde gösterir.
- Teknik olmayan kullanıcı için ekran metinleri anlaşılırdır.

## Bağımlılıklar

- EPIC-02 Tıklama Motoru ve Hız Kontrolü
- EPIC-03 Güvenli Başlatma / Durdurma ve Kısayol
- EPIC-04 Pencere Hedefleme ve Odak Koruması
- EPIC-05 Sayaç, Süre ve Durma Sebebi

