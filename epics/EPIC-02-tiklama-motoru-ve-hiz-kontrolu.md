# EPIC-02 — Tıklama Motoru ve Hız Kontrolü

## Amaç

Kullanıcının belirlediği hızda sol tık otomasyonu çalıştıran, sayaç ve durdurma komutlarıyla uyumlu temel otomasyon davranışını tanımlamak.

## MVP Kapsamı

- Sol tık otomasyonu
- Saniyedeki tıklama sayısı veya tıklamalar arası bekleme değeri
- Geçerli hız aralığı ve hatalı değer kontrolleri
- Sınırsız çalıştırma modu
- Kullanıcı durdurana veya güvenlik koşulu tetiklenene kadar çalışma
- Her başarılı tıklamada sayaç olayının üretilmesi

## Kapsam Dışı

- Sağ tık ve çift tık
- Klavye otomasyonu
- Mouse hareketi kaydı
- Gelişmiş zamanlama senaryoları
- Görsel veya OCR tetikli tıklama

## Kabul Kriterleri

- Otomasyon başlatıldığında seçilen hızda sol tık üretir.
- Geçersiz hız değerleriyle otomasyon başlatılmaz.
- Stop komutu geldiğinde tıklama üretimi güvenli şekilde durur.
- Tıklama motoru pencere odağı ve global kısayol akışından gelen durdurma sinyallerini dikkate alır.
- Toplam tıklama sayacı yalnızca gerçekleştirilen tıklamalarla artar.

## Bağımlılıklar

- EPIC-03 Güvenli Başlatma / Durdurma ve Kısayol
- EPIC-04 Pencere Hedefleme ve Odak Koruması
- EPIC-05 Sayaç, Süre ve Durma Sebebi

