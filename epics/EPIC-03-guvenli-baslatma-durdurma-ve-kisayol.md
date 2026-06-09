# EPIC-03 — Güvenli Başlatma / Durdurma ve Kısayol

## Amaç

Otomasyonun kullanıcı kontrolü dışında kalmasını engelleyen, hem arayüz hem global kısayol üzerinden güvenli başlatma ve durdurma akışını tanımlamak.

## MVP Kapsamı

- Start / Stop buton davranışı
- Tek global başlat / durdur kısayolu
- Çalışırken tekrar start verilmesini engelleme
- Durdurma komutunun her zaman öncelikli olması
- Kullanıcının farkında olmadan arka planda otomasyon başlamasını engelleme
- Kısayol çakışması veya geçersiz kısayol durumlarının kullanıcıya bildirilmesi

## Kapsam Dışı

- Birden fazla kısayol profili
- Kısayol kombinasyonu kayıt geçmişi
- Rol bazlı güvenlik
- Kurumsal politika yönetimi

## Kabul Kriterleri

- Kullanıcı butonla veya kısayolla otomasyonu başlatabilir.
- Kullanıcı butonla veya kısayolla otomasyonu durdurabilir.
- Stop komutu, tıklama döngüsünden daha yüksek öncelikli çalışır.
- Geçersiz veya kullanılamayan kısayol durumunda otomasyon başlamaz.
- Otomasyonun son durma sebebi kullanıcıya gösterilir.

## Bağımlılıklar

- EPIC-01 Uygulama Kontrol Yüzeyi
- EPIC-02 Tıklama Motoru ve Hız Kontrolü
- EPIC-05 Sayaç, Süre ve Durma Sebebi

