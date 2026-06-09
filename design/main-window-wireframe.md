# TASK-002 — PySide6 Ana Pencere Wireframe

## Amaç

Turkuaz ClickFlow MVP ana penceresinde yer alacak alanları, kullanıcı akışını ve ekran durumlarına göre davranışları tanımlamak.

Bu belge kod değildir. PySide6 ile uygulanacak ana pencerenin ürün ve bilgi mimarisi çıktısıdır.

## Tasarım İlkeleri

- Kullanıcı tek ekrandan otomasyonu başlatıp durdurabilmelidir.
- Stop kontrolü otomasyon çalışırken en görünür ve en erişilebilir aksiyon olmalıdır.
- CPS, kısayol, sayaç, süre ve durum bilgisi teknik olmayan kullanıcı için anlaşılır olmalıdır.
- Pencere seçimi ve pencere koruması Sprint-1 minimum çıkışı için bloklayıcı değildir.
- UI PySide6 ile tasarlanacaktır; ürün mantığı, sayaç ve durum makinesi UI katmanına gömülmemelidir.

## Ana Pencere Alanları

### 1. Başlık Alanı

Gösterilecek bilgiler:

- Ürün adı: `Turkuaz ClickFlow`
- Kısa durum etiketi: `Hazır`, `Çalışıyor`, `Durdu`, `Hata`

Amaç:

- Kullanıcının uygulamanın ne durumda olduğunu ilk bakışta anlaması.

### 2. Ana Kontrol Alanı

Kontroller:

- `Start` butonu
- `Stop` butonu
- Varsayılan kısayol göstergesi: `F8`

Davranış:

- `Start`, geçerli ayarlar varsa otomasyonu başlatır.
- `Stop`, otomasyon çalışırken aktif ve öncelikli olur.
- `F8`, otomasyon duruyorken başlatır; çalışıyorken durdurur.

### 3. Hız Ayarı Alanı

Alanlar:

- CPS giriş alanı
- Minimum değer notu: `Min: 1`
- Maksimum değer notu: `Max: 100`
- Varsayılan değer: `10`

Davranış:

- Geçerli aralık: 1-100 CPS.
- Geçersiz CPS değerinde Start pasif olur veya Start denemesinde uyarı gösterilir.
- Sprint-1 için hız değişikliğinin çalışırken uygulanması zorunlu değildir; güvenli varsayım, değişikliklerin yeni başlatmada geçerli olmasıdır.

### 4. Pencere Seçimi Alanı

Alanlar:

- Hedef pencere seçimi: opsiyonel
- Pencere koruması seçeneği: opsiyonel
- Hedef pencere durumu: `Seçilmedi` veya seçilen pencere adı

Davranış:

- Hedef pencere seçilmeden otomasyon başlatılabilir.
- Pencere koruması kapalıysa hedef pencere kontrolü yapılmaz.
- Pencere koruması açık ve hedef pencere geçersizse otomasyon başlatılmaz veya çalışırken güvenli şekilde durur.
- TASK-007 ve TASK-008 Sprint-1 minimum çıkışının bloklayıcısı değildir; alanlar geleceğe uyum için wireframe'de yer alır.

### 5. Sayaç ve Süre Alanı

Gösterilecek bilgiler:

- Toplam tıklama sayısı
- Çalışma süresi

Davranış:

- Her yeni çalıştırmada sayaç sıfırlanır.
- Sayaç sadece gerçekleşen tıklamalarda artar.
- Stop sonrası son sayaç ve süre değerleri görünür kalır.
- Yeni Start verildiğinde sayaç tekrar 0'dan başlar.

### 6. Durum ve Uyarı Alanı

Gösterilecek bilgiler:

- Mevcut durum
- Son durma sebebi
- Geçersiz ayar uyarısı
- Kısayol kullanılamıyor uyarısı
- Platform adapter kaynaklı hata mesajı

Mesaj dili:

- Kısa
- Kullanıcı aksiyonuna dönük
- Teknik ayrıntıya boğulmadan anlaşılır

Örnek mesajlar:

- `Hazır. Başlatmak için Start'a basın veya F8 kullanın.`
- `Çalışıyor. Durdurmak için Stop'a basın veya F8 kullanın.`
- `Durdu. Son durma sebebi: Kullanıcı durdurdu.`
- `CPS değeri 1 ile 100 arasında olmalıdır.`
- `Kısayol kullanılamıyor. F8 başka bir uygulama tarafından kullanılıyor olabilir.`

## Wireframe

```text
┌──────────────────────────────────────────────────────────────┐
│ Turkuaz ClickFlow                              Durum: Hazır   │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Kontrol                                                     │
│  ┌──────────────┐  ┌──────────────┐  Kısayol: F8             │
│  │    Start     │  │     Stop     │                          │
│  └──────────────┘  └──────────────┘                          │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│  Hız Ayarı                                                   │
│  CPS: [ 10 ]       Min: 1     Max: 100                       │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│  Pencere                                                     │
│  Hedef pencere: [ Seçilmedi                       v ]         │
│  [ ] Pencere değişince durdur                                │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│  Çalışma Bilgisi                                             │
│  Tıklama sayısı: 0                                           │
│  Çalışma süresi: 00:00:00                                    │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│  Mesaj                                                       │
│  Hazır. Başlatmak için Start'a basın veya F8 kullanın.        │
└──────────────────────────────────────────────────────────────┘
```

## Kullanıcı Akışı

### Akış 1 — Varsayılan Ayarla Başlatma

1. Kullanıcı uygulamayı açar.
2. Ana pencere `Hazır` durumunda görünür.
3. CPS alanı varsayılan `10` değerini gösterir.
4. Kısayol alanı `F8` değerini gösterir.
5. Kullanıcı `Start` butonuna basar veya `F8` kullanır.
6. Otomasyon çalışmaya başlar.
7. Durum `Çalışıyor` olur.
8. Sayaç 0'dan başlar ve gerçekleşen tıklamalarla artar.
9. Çalışma süresi ilerler.

### Akış 2 — Durdurma

1. Otomasyon çalışıyordur.
2. Kullanıcı `Stop` butonuna basar veya `F8` kullanır.
3. Otomasyon güvenli şekilde durur.
4. Durum `Durdu` olur.
5. Son sayaç ve çalışma süresi görünür kalır.
6. Son durma sebebi `Kullanıcı durdurdu` veya `F8 ile durduruldu` olarak gösterilir.

### Akış 3 — Geçersiz CPS

1. Kullanıcı CPS alanına 1'den küçük veya 100'den büyük değer girer.
2. Ekran CPS değerinin geçersiz olduğunu belirtir.
3. Otomasyon başlatılmaz.
4. Mesaj alanında `CPS değeri 1 ile 100 arasında olmalıdır.` gösterilir.

### Akış 4 — Yeni Çalıştırma

1. Önceki çalıştırma durmuştur.
2. Kullanıcı tekrar `Start` veya `F8` ile başlatır.
3. Sayaç 0'a sıfırlanır.
4. Çalışma süresi yeniden başlar.

### Akış 5 — Opsiyonel Pencere Koruması

1. Kullanıcı hedef pencere seçebilir veya seçmeden devam edebilir.
2. Pencere koruması kapalıysa otomasyon pencere kontrolü olmadan çalışır.
3. Pencere koruması açıksa hedef pencere seçimi gerekir.
4. Hedef pencere değişirse veya kapanırsa otomasyon durur.
5. Mesaj alanında pencere kaynaklı durma sebebi gösterilir.

## Ekran Durumları

### Hazır

Koşul:

- Uygulama açık, otomasyon çalışmıyor.
- CPS geçerli veya varsayılan değerde.

Ekran davranışı:

- `Start` aktif.
- `Stop` pasif veya ikincil görünümde.
- CPS alanı düzenlenebilir.
- Pencere alanı düzenlenebilir.
- Sayaç son değerini gösterebilir; yeni Start ile sıfırlanacağı açık davranıştır.
- Mesaj: `Hazır. Başlatmak için Start'a basın veya F8 kullanın.`

### Çalışıyor

Koşul:

- Otomasyon aktif.

Ekran davranışı:

- `Start` pasif.
- `Stop` aktif ve öncelikli.
- CPS alanı tercihen kilitli veya değişikliğin sonraki çalıştırmada geçerli olacağı belirtilmiş.
- Sayaç artar.
- Süre ilerler.
- Mesaj: `Çalışıyor. Durdurmak için Stop'a basın veya F8 kullanın.`

### Durduruluyor

Koşul:

- Stop komutu alınmış, tıklama döngüsü güvenli kapanmaktadır.

Ekran davranışı:

- `Start` pasif.
- `Stop` pasif veya bekleme durumunda.
- Sayaç son güvenli değerde kalır.
- Mesaj: `Durduruluyor...`

### Durdu

Koşul:

- Otomasyon kullanıcı komutu veya güvenlik koşulu ile durmuştur.

Ekran davranışı:

- `Start` aktif.
- `Stop` pasif.
- Sayaç ve süre son değerleri gösterir.
- Mesaj son durma sebebini gösterir.

Örnek durma sebepleri:

- `Kullanıcı durdurdu`
- `F8 ile durduruldu`
- `Pencere değişti`
- `Hedef pencere bulunamadı`
- `Hata nedeniyle durdu`

### Hata

Koşul:

- Otomasyon başlatılamamış veya çalışırken hata oluşmuştur.

Ekran davranışı:

- `Start`, hata türüne göre aktif veya pasif olabilir.
- `Stop` otomasyon çalışmıyorsa pasif olur.
- Mesaj alanı kullanıcı aksiyonunu belirtir.

Örnek:

- `Kısayol kullanılamıyor. F8 başka bir uygulama tarafından kullanılıyor olabilir.`
- `CPS değeri 1 ile 100 arasında olmalıdır.`
- `Otomatik tıklama başlatılamadı. Lütfen tekrar deneyin.`

## Kontrol Davranış Matrisi

| Durum | Start | Stop | F8 | CPS Alanı | Sayaç | Süre |
| --- | --- | --- | --- | --- | --- | --- |
| Hazır | Aktif | Pasif | Başlatır | Düzenlenebilir | Son değer veya 0 | Son değer veya 0 |
| Çalışıyor | Pasif | Aktif | Durdurur | Kilitli veya sonraki çalıştırma için | Artar | İlerler |
| Durduruluyor | Pasif | Pasif | İşlem yok veya bekler | Kilitli | Son değer | Son değer |
| Durdu | Aktif | Pasif | Başlatır | Düzenlenebilir | Son değer | Son değer |
| Hata | Hata türüne bağlı | Pasif | Hata türüne bağlı | Düzenlenebilir | Son değer | Son değer |

## PySide6 Uygulama Notları

Bu bölüm uygulama kodu değildir; UI uygulanırken kullanılabilecek yapı kararlarını belirtir.

- Ana pencere tek `MainWindow` olarak düşünülmelidir.
- Kontrol alanları tek ekranda kalmalıdır.
- Mesaj alanı pencerenin alt kısmında sabit ve okunabilir olmalıdır.
- UI katmanı sadece kullanıcı girdisini toplamalı ve görünür durumu yansıtmalıdır.
- Durum makinesi, sayaç ve CPS doğrulama domain/app katmanından gelmelidir.

## TASK-002 Kabul Kontrolü

- Ana ekranda gösterilecek tüm MVP alanları tanımlandı.
- Start, Stop, F8, CPS, sayaç, süre, pencere ve mesaj alanlarının davranışı tanımlandı.
- Hazır, çalışıyor, durduruluyor, durdu ve hata durumları belirlendi.
- UI geliştirmeye başlamadan önce ürün davranışı anlaşılır hale getirildi.

