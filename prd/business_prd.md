# Business PRD — Turkuaz ClickFlow

## 1. Ürün Adı

Turkuaz ClickFlow

## 2. Ürün Kısa Açıklaması

Turkuaz ClickFlow, kullanıcı tarafından belirlenen tıklama, klavye ve ekran etkileşimlerini otomatik olarak gerçekleştiren bir masaüstü otomasyon uygulamasıdır.

Ürün; tekrar eden mouse tıklamaları, belirli aralıklarla yapılan işlemler, pencere bazlı otomasyonlar ve kullanıcı tarafından başlatılıp durdurulabilen görev akışları için kullanılacaktır.

## 3. Ürün Hangi Problemi Çözüyor?

Kullanıcılar bazı masaüstü işlemlerinde aynı tıklamaları veya klavye işlemlerini sürekli tekrar etmek zorunda kalmaktadır.

Bu durum:

- Zaman kaybına neden olur
- Kullanıcıyı yorar
- Manuel hata riskini artırır
- Uzun süren tekrar eden işlemleri verimsiz hale getirir

Turkuaz ClickFlow, bu tekrar eden işlemleri otomatikleştirerek kullanıcıya hız ve kolaylık sağlar.

## 4. Ürünün Temel Amacı

Ürünün temel amacı, kullanıcının belirlediği mouse ve klavye işlemlerini insan müdahalesi olmadan, ayarlanan hızda ve kontrollü şekilde gerçekleştirmektir.

Ana amaçlar:

- Tekrarlayan işlemleri hızlandırmak
- Kullanıcı iş yükünü azaltmak
- Tıklama ve klavye aksiyonlarını otomatikleştirmek
- Başlat/durdur kontrollü güvenli bir otomasyon sağlamak
- Belirli pencere veya ekran durumlarına göre çalışabilmek

## 5. Kim Kullanacak?

### Bireysel Kullanıcılar

Tekrar eden tıklama ve klavye işlemlerini otomatikleştirmek isteyen kullanıcılar.

### Operasyon Kullanıcıları

Masaüstü programlarda sürekli tekrar eden işlemleri hızlandırmak isteyen ekipler.

### Test Kullanıcıları

Uygulama arayüzlerinde tekrar eden tıklama ve işlem senaryolarını test etmek isteyen kişiler.

### Firma İçi Personel

Belirli masaüstü görevlerini daha hızlı yapmak isteyen çalışanlar.

## 6. Kaç Farklı Kullanıcı Rolü Var?

İlk versiyonda tek kullanıcı tipi olacaktır:

### Standart Kullanıcı

- Programı açar
- Tıklama ayarlarını yapar
- Başlatır
- Durdurur
- Hedef pencereyi seçer
- Hız ayarını yapar

İlerleyen versiyonlarda admin, profil yöneticisi veya kurumsal kullanıcı rolleri eklenebilir.

## 7. Kullanıcı Üründe Ne Yapabilecek?

Kullanıcı:

- Otomatik tıklama başlatabilecek
- Otomatik tıklamayı durdurabilecek
- Tıklama hızını belirleyebilecek
- Saniyedeki tıklama sayısını ayarlayabilecek
- Belirli bir pencereyi hedef olarak seçebilecek
- Başka pencereye geçildiğinde işlemi durdurabilecek
- Klavye kısayolu ile başlatma/durdurma yapabilecek
- Start / Stop butonlarıyla kontrol sağlayabilecek
- Tıklama türünü seçebilecek
- Sol tık / sağ tık / çift tık gibi seçenekleri belirleyebilecek
- Belirli koordinata tıklama yapabilecek
- Mouse’un mevcut konumuna tıklama yaptırabilecek

## 8. Ürüne Veri Nereden Gelecek?

Kullanıcı uygulama üzerinden şu bilgileri girecektir:

- Tıklama hızı
- Tıklama türü
- Hedef pencere
- Başlatma/durdurma tuşu
- Tıklama koordinatı
- Çalışma modu
- Durma koşulları

## 9. Ürün Kullanıcıdan Ne İsteyecek?

Ürün kullanıcıdan şu ayarları isteyecektir:

- Kaç tıklama yapılacak?
- Tıklama süresi sınırsız mı olacak?
- Saniyede kaç tıklama yapılacak?
- Hangi mouse tuşu kullanılacak?
- Hangi pencere hedeflenecek?
- Başka pencereye geçilirse duracak mı?
- Hangi tuş ile başlatılıp durdurulacak?
- Tıklama mevcut mouse konumunda mı yapılacak, sabit koordinatta mı?

## 10. Ürün Çıktı Olarak Ne Verecek?

Ürün kullanıcıya şu çıktıları gösterecektir:

- Otomasyon çalışıyor / durdu durumu
- Toplam yapılan tıklama sayısı
- Geçen süre
- Aktif hedef pencere
- Seçilen tıklama hızı
- Hata veya uyarı mesajları
- Durma sebebi

## 11. Üründe Hangi Özellikler Olmalı?

### Otomatik Mouse Tıklama

Kullanıcı tarafından belirlenen hızda otomatik tıklama yapılmalıdır.

### Hız Ayarı

Kullanıcı saniyedeki tıklama sayısını veya tıklamalar arası bekleme süresini belirleyebilmelidir.

### Start / Stop Kontrolü

Kullanıcı uygulama üzerinden başlatma ve durdurma yapabilmelidir.

### Klavye Kısayolu

Kullanıcı belirlenen bir tuş ile otomasyonu başlatıp durdurabilmelidir.

### Pencere Seçme

Kullanıcı otomasyonun çalışacağı hedef pencereyi seçebilmelidir.

### Pencere Değişince Durma

Kullanıcı başka bir pencereye geçtiğinde otomasyon otomatik olarak durabilmelidir.

### Tıklama Tipi Seçimi

Sol tık, sağ tık, çift tık gibi seçenekler olmalıdır.

### Koordinat Seçimi

Kullanıcı tıklamanın yapılacağı ekran konumunu belirleyebilmelidir.

### Sayaç

Toplam yapılan tıklama sayısı gösterilmelidir.

### Güvenli Durdurma

Kullanıcı her an otomasyonu hızlıca durdurabilmelidir.

## 12. Olmazsa Olmaz Özellikler

İlk MVP için gerekli özellikler:

- Masaüstü uygulaması
- Start / Stop butonu
- Klavye kısayolu ile başlatma/durdurma
- Tıklama hızı ayarı
- Sol tık otomasyonu
- Toplam tıklama sayacı
- Başka pencereye geçince durma seçeneği
- Basit ve anlaşılır arayüz

## 13. İleride Eklenmesi İstenen Özellikler

Gelecek versiyonlarda:

- Klavye makro kaydı
- Mouse hareketi kaydı
- Senaryo kaydetme
- Profil oluşturma
- Zamanlanmış otomasyon
- Görüntü tanıma ile tıklama
- Belirli buton veya görsel bulununca tıklama
- Çok adımlı makro oluşturma
- Log kayıtları
- Kurumsal lisanslama
- Türkçe / İngilizce dil desteği

## 14. Kullanıcı Ürünü Nasıl Kullanacak?

1. Kullanıcı uygulamayı açar.
2. Tıklama hızını belirler.
3. Tıklama türünü seçer.
4. Hedef pencereyi seçer.
5. Başlatma/durdurma kısayolunu belirler.
6. Start butonuna basar veya kısayol tuşunu kullanır.
7. Program otomatik tıklamaya başlar.
8. Kullanıcı Stop butonu veya kısayol ile işlemi durdurur.
9. Program toplam tıklama sayısını ve çalışma süresini gösterir.

## 15. Ürün Kullanıcının Hangi Kararını Kolaylaştıracak?

Ürün, kullanıcının tekrar eden işlemleri manuel mi yapacağı yoksa otomasyona mı bırakacağı kararını kolaylaştırır.

Ayrıca kullanıcıya:

- Ne kadar tıklama yapıldığını
- Otomasyonun ne kadar sürdüğünü
- İşlemin hangi pencere üzerinde çalıştığını
- İşlemin güvenli şekilde durup durmadığını

gösterir.

## 16. Başarı Nasıl Ölçülecek?

Ürün başarılı sayılırsa:

- Kullanıcı tek tıkla otomasyonu başlatabiliyorsa
- Program stabil çalışıyorsa
- Tıklama hızı doğru uygulanıyorsa
- Kullanıcı istediği anda durdurabiliyorsa
- Başka pencereye geçildiğinde durma özelliği çalışıyorsa
- Arayüz teknik olmayan kullanıcılar için anlaşılırsa

## 17. Benzer Sistemler Var mı?

Benzer sistemler:

- Auto Clicker uygulamaları
- Macro Recorder uygulamaları
- Mouse automation araçları

Turkuaz ClickFlow’un farkı:

- Daha sade arayüz
- Pencere bazlı çalışma
- Güvenli durdurma
- Türkçe kullanım
- İleride görüntü tanıma ve senaryo bazlı akış desteği

## 18. Özellikle İstenmeyen Şeyler

Üründe istenmeyen şeyler:

- Karmaşık ayarlar
- Teknik bilgi gerektiren kullanım
- Kontrolsüz çalışan otomasyon
- Durdurulamayan işlem
- Kullanıcının farkında olmadan arka planda işlem yapması
- Hedef pencere dışında tıklama yapması

## 19. Örnek Ekran Yapısı

Ana ekran:

- Program adı
- Start butonu
- Stop butonu
- Tıklama hızı ayarı
- Tıklama tipi seçimi
- Hedef pencere seçimi
- Kısayol tuşu seçimi
- Toplam tıklama sayısı
- Çalışma süresi
- Durum göstergesi

## 20. Ürünün Tek Cümlelik Başarı Tanımı

Turkuaz ClickFlow, kullanıcının tekrar eden mouse ve klavye işlemlerini güvenli, kontrollü ve ayarlanabilir hızda otomatik olarak gerçekleştirmesini sağlamalıdır.

## Platform Kararı

Turkuaz ClickFlow hem Windows hem macOS üzerinde çalışacak şekilde tasarlanacaktır.

MVP hedefi:

- Windows desteği
- macOS için temel uyumluluk hazırlığı

Ürün mimarisinde mouse, klavye ve pencere işlemleri platforma özel adapter yapısıyla ayrılacaktır.

Windows ve macOS aynı arayüzü kullanacak; ancak pencere listeleme, global kısayol ve otomatik tıklama işlemleri işletim sistemine göre ayrı uygulanacaktır.

## Ürün Sahibi Kararı

Turkuaz ClickFlow hem Windows hem macOS destekleyecek şekilde tasarlanacaktır.

Kod mimarisinde platforma özel işlemler adapter yapısına ayrılmalıdır:

- Windows adapter
- macOS adapter

Ortak ürün mantığı, sayaç, durum makinesi ve UI platformdan bağımsız olmalıdır.

İlk geliştirme Windows odaklı yapılabilir; ancak macOS desteği mimaride baştan düşünülmelidir.
