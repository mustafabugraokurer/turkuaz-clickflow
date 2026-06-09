# EPIC-05 — Sayaç, Süre ve Durma Sebebi

## Amaç

Kullanıcının otomasyonun ne kadar çalıştığını, kaç tıklama yaptığını ve neden durduğunu güvenle anlayacağı geri bildirimleri tanımlamak.

## MVP Kapsamı

- Toplam tıklama sayacı
- Çalışma süresi
- Aktif durum göstergesi
- Son durma sebebi
- Basit hata ve uyarı mesajları
- Her yeni çalıştırmada sayaç/süre davranışının net olması

## Kapsam Dışı

- Kalıcı log kayıtları
- Oturum geçmişi
- Dışa aktarma
- Analitik paneli

## Kabul Kriterleri

- Otomasyon çalışırken sayaç görünür şekilde artar.
- Çalışma süresi otomasyon boyunca güncellenir.
- Stop, kısayol, pencere değişimi ve hata gibi durma sebepleri ayırt edilir.
- Yeni çalışma başlatıldığında sayaç ve süre davranışı kullanıcı beklentisine uygun şekilde sıfırlanır veya açıkça korunur.
- Hata mesajları teknik ayrıntı yerine kullanıcı aksiyonuna odaklanır.

## Bağımlılıklar

- EPIC-02 Tıklama Motoru ve Hız Kontrolü
- EPIC-03 Güvenli Başlatma / Durdurma ve Kısayol
- EPIC-04 Pencere Hedefleme ve Odak Koruması

