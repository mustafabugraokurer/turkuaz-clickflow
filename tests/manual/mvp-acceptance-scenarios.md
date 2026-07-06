# MVP Manuel Dogrulama Senaryolari

## Durum Notu

Bu belge TASK-011 kapsaminda manuel kabul senaryolarini tanimlar.

TASK-001 kapanisi ve Windows smoke test sonrasi durum:

- PySide6 ana pencere ve UI/app baglantisi olusturulmustur.
- Windows global hotkey adapter katmani olusturulmustur.
- ClickRunner app katmaninda test edilebilir sekilde olusturulmustur.
- UI Start / Stop ve F8 akisi ClickRunner calisma dongusune baglanmistir.
- Windows mouse backend'i TASK-019 ile gercek `SendInput` backend'ine alinmistir; Windows disi ortamda guvenli unavailable backend davranisi vardir.
- macOS mouse backend'i TASK-022 ile gercek Quartz backend'ine alinmistir; Accessibility veya Input Monitoring izni gerekebilir.
- Gercek Windows OS davranisi TASK-021 smoke testinde Passed sonuc vermistir.
- macOS izin ve global hotkey davranisi ayrica dogrulanmalidir.

Bu nedenle senaryolar ikiye ayrilmistir:

1. Su an unit/app seviyesinde dogrulanabilir senaryolar
2. UI + platform adapter geldikten sonra manuel dogrulanacak senaryolar

## 1. Su An Unit/App Seviyesinde Dogrulanabilir Senaryolar

Bu senaryolar gercek UI veya gercek mouse tiklama gerektirmez. Mevcut Python app/domain servisleri ve unit test kapsami ile dogrulanabilir.

### S1 — Varsayilan Ayarlar

Amac:

Varsayilan MVP degerlerinin dogru oldugunu dogrulamak.

On kosullar:

- Domain katmani mevcut.
- `AutomationSettings.defaults()` kullanilabilir.

Adimlar:

1. Varsayilan ayarlari olustur.
2. CPS degerini kontrol et.
3. Hotkey degerini kontrol et.

Beklenen sonuc:

- CPS `10` olur.
- Hotkey `F8` olur.
- Pencere secimi bos olabilir.
- Pencere korumasi kapali olabilir.

Mevcut dogrulama:

- `tests/unit/test_cps_policy.py`

### S2 — CPS Araligi

Amac:

1-100 CPS araliginin kabul edildigini, aralik disi degerlerin reddedildigini dogrulamak.

Adimlar:

1. CPS `1` ile ayar olustur.
2. CPS `10` ile ayar olustur.
3. CPS `100` ile ayar olustur.
4. CPS `0`, `-1` ve `101` ile ayar olusturmayi dene.

Beklenen sonuc:

- `1`, `10`, `100` kabul edilir.
- `0`, `-1`, `101` reddedilir.
- Gecersiz CPS, kullaniciya "CPS degeri 1 ile 100 arasinda olmalidir." mesaji olarak yansitilabilir.

Mevcut dogrulama:

- `tests/unit/test_cps_policy.py`
- `tests/unit/test_feedback_service.py`

### S3 — Start Durum Gecisi

Amac:

Otomasyonun baslangic durumundan calisir duruma gecebildigini dogrulamak.

Adimlar:

1. `AutomationService` olustur.
2. Baslangic durumunu kontrol et.
3. Gecerli CPS ile `start` komutu ver.

Beklenen sonuc:

- Baslangic durumu `READY` olur.
- Start sonrasi durum `RUNNING` olur.
- Start sonucu kabul edilir.

Mevcut dogrulama:

- `tests/unit/test_automation_service.py`

### S4 — Tekrar Start Yeni Dongu Baslatmaz

Amac:

Otomasyon calisirken tekrar start verilirse ikinci bir run baslatilmadigini dogrulamak.

Adimlar:

1. `AutomationService` olustur.
2. `start` komutu ver.
3. Tekrar `start` komutu ver.
4. Run sayisini ve ayarlari kontrol et.

Beklenen sonuc:

- Ilk start yeni run baslatir.
- Ikinci start kabul edilse bile yeni run baslatmaz.
- Run sayisi 1 kalir.
- Mevcut calisma ayarlari korunur.

Mevcut dogrulama:

- `tests/unit/test_automation_service.py`

### S5 — Stop ve Durma Sebebi

Amac:

Calisir durumdayken stop komutunun otomasyonu durdurdugunu ve durma sebebi urettigini dogrulamak.

Adimlar:

1. `AutomationService` olustur.
2. `start` komutu ver.
3. `stop` komutu ver.
4. Durum ve stop reason degerlerini kontrol et.

Beklenen sonuc:

- Durum `STOPPED` olur.
- Varsayilan durma sebebi `USER_STOPPED` olur.
- Stop sonucu kabul edilir.

Mevcut dogrulama:

- `tests/unit/test_automation_service.py`

### S6 — F8 Toggle Davranisi

Amac:

F8 tetiklenince otomasyon duruyorsa baslatma, calisiyorsa durdurma davranisinin dogru oldugunu dogrulamak.

Adimlar:

1. `AutomationService` olustur.
2. `HotkeyService` olustur.
3. `F8` tetikle.
4. Tekrar `F8` tetikle.

Beklenen sonuc:

- Ilk `F8`, otomasyonu `RUNNING` durumuna getirir.
- Ikinci `F8`, otomasyonu `STOPPED` durumuna getirir.
- Ikinci tetiklemede durma sebebi `HOTKEY_STOPPED` olur.

Mevcut dogrulama:

- `tests/unit/test_hotkey_service.py`

### S7 — Gecersiz Kisa Yol

Amac:

F8 disindaki tetiklerin app seviyesinde reddedildigini dogrulamak.

Adimlar:

1. `HotkeyService` olustur.
2. `F7` veya baska bir kisa yol tetikle.

Beklenen sonuc:

- Tetik reddedilir.
- Otomasyon baslamaz.
- Kullanici mesaji kisa yolun kullanilamadigini belirtir.

Mevcut dogrulama:

- `tests/unit/test_hotkey_service.py`
- `tests/unit/test_feedback_service.py`

### S8 — Sayac Yeni Calistirmada Sifirlanir

Amac:

Yeni otomasyon calistirmasinda sayacin sifirlandigini dogrulamak.

Adimlar:

1. `AutomationService` veya `ClickCounter` olustur.
2. Sayaci artir.
3. Yeni run baslat.

Beklenen sonuc:

- Yeni run basladiginda sayac `0` olur.
- Stop sonrasi son sayac degeri korunabilir.

Mevcut dogrulama:

- `tests/unit/test_counter.py`
- `tests/unit/test_automation_service.py`

### S9 — Basarili Tiklama Olayi Sayaci Artirir

Amac:

Gelecekteki tiklama motorundan gelecek basarili tiklama olaylarinin sayaca baglanabildigini dogrulamak.

Adimlar:

1. `AutomationService` olustur.
2. `start` komutu ver.
3. `record_successful_click` cagir.

Beklenen sonuc:

- Calisir durumda basarili tiklama kaydi sayaci artirir.
- Calisir durumda degilken tiklama kaydi reddedilir.

Mevcut dogrulama:

- `tests/unit/test_automation_service.py`

### S10 — Calisma Suresi

Amac:

Calisma suresinin run baslangicinda sifirlandigini, calisirken ilerledigini ve stop sonrasi dondugunu dogrulamak.

Adimlar:

1. Test clock ile `TimerService` olustur.
2. Yeni run baslat.
3. Clock degerini ilerlet.
4. Stop ver.
5. Clock degerini tekrar ilerlet.

Beklenen sonuc:

- Yeni run baslangicinda sure `0` olur.
- Calisirken sure ilerler.
- Stop sonrasi sure son degerde kalir.

Mevcut dogrulama:

- `tests/unit/test_timer_service.py`
- `tests/unit/test_automation_service.py`

### S11 — Durum ve Uyari Mesajlari

Amac:

Hazir, calisiyor, durdu, hata ve durma sebebi mesajlarinin kullaniciya uygun oldugunu dogrulamak.

Adimlar:

1. `FeedbackService` olustur.
2. `READY`, `RUNNING`, `STOPPED`, `ERROR` durumlari icin mesaj al.
3. `USER_STOPPED`, `HOTKEY_STOPPED`, `INVALID_SETTINGS`, `WINDOW_CHANGED`, `TARGET_WINDOW_MISSING`, `ERROR` sebepleri icin mesaj al.

Beklenen sonuc:

- Mesajlar teknik ayrintiya bogulmaz.
- Kullanici ne oldugunu ve gerekiyorsa neyi duzeltmesi gerektigini anlar.

Mevcut dogrulama:

- `tests/unit/test_feedback_service.py`

## 2. UI + Platform Adapter Geldikten Sonra Manuel Dogrulanacak Senaryolar

Bu senaryolar gerçek Windows ortamında, gerçek mouse backend'i ve UI ClickRunner çalışma döngüsü tamamlandıktan sonra çalıştırılmalıdır.

### M1 — Uygulama Acilisi ve Ana Ekran

Amac:

PySide6 ana pencerenin MVP wireframe'e uygun acildigini dogrulamak.

On kosullar:

- PySide6 UI implementasyonu tamamlanmis.

Adimlar:

1. Uygulamayi baslat.
2. Ana pencereyi incele.

Beklenen sonuc:

- Urun adi `Turkuaz ClickFlow` gorunur.
- Durum `Hazir` olarak gorunur.
- Start ve Stop kontrolleri gorunur.
- CPS alani varsayilan `10` gosterir.
- Kisa yol `F8` olarak gorunur.
- Tiklama sayaci ve calisma suresi gorunur.
- Mesaj alani hazir mesajini gosterir.

### M2 — Start Butonu ile Baslatma

Amac:

UI Start kontrolunun app katmaninda start davranisini tetikledigini dogrulamak.

On kosullar:

- PySide6 UI implementasyonu tamamlanmis.
- AutomationService UI'a baglanmis.

Adimlar:

1. Uygulamayi ac.
2. CPS degerini `10` olarak birak.
3. Start butonuna bas.

Beklenen sonuc:

- Durum `Calisiyor` olur.
- Start pasif olur.
- Stop aktif olur.
- Calisma suresi ilerlemeye baslar.
- Sayac yeni calistirmada `0` olur.

Not:

Gercek mouse tiklama motoru yoksa sayacin otomatik artmasi beklenmez; sadece start/sure davranisi dogrulanir.

### M3 — Stop Butonu ile Durdurma

Amac:

UI Stop kontrolunun guvenli durdurma davranisini tetikledigini dogrulamak.

On kosullar:

- Uygulama calisir durumda.

Adimlar:

1. Stop butonuna bas.

Beklenen sonuc:

- Durum `Durdu` olur.
- Stop pasif olur.
- Start tekrar aktif olur.
- Calisma suresi son degerde kalir.
- Mesaj son durma sebebini `Kullanici durdurdu` olarak gosterir.

### M4 — Gercek F8 Global Kisa Yol

Amac:

OS seviyesinde F8 global kisa yolunun uygulamaya baglandigini dogrulamak.

On kosullar:

- Windows/macOS global hotkey adapter implementasyonu tamamlanmis.
- Uygulama arka plandayken hotkey dinleyebiliyor.

Adimlar:

1. Uygulamayi ac.
2. F8'e bas.
3. Uygulama calisir duruma gecsin.
4. Baska pencereye gec.
5. F8'e tekrar bas.

Beklenen sonuc:

- Ilk F8 otomasyonu baslatir.
- Ikinci F8 otomasyonu durdurur.
- Durma sebebi `F8 ile durduruldu` olarak gorunur.
- Uygulama odakta degilken de kisa yol calisir.

### M5 — Gecersiz veya Kullanilamayan Kisa Yol

Amac:

Kisa yol kullanilamiyorsa kullanicinin anlasilir sekilde uyarildigini dogrulamak.

On kosullar:

- UI kisa yol ayari veya adapter hata geri bildirimi tamamlanmis.

Adimlar:

1. F8'in OS veya baska uygulama tarafindan kullanilamadigi bir durumu simule et.
2. Otomasyonu baslatmayi dene.

Beklenen sonuc:

- Otomasyon sessizce baslamaz.
- Mesaj alani kisa yolun kullanilamadigini belirtir.

### M6 — Gercek Mouse Tiklama ve CPS

Amac:

Mouse tiklama motorunun secilen CPS degerine uygun calistigini dogrulamak.

On kosullar:

- Mouse tiklama adapter'i ve tiklama motoru tamamlanmis.
- Test edilecek guvenli bir hedef alan hazir.

Adimlar:

1. CPS degerini `1` yap.
2. Otomasyonu baslat ve kisa sure gozlemle.
3. Otomasyonu durdur.
4. CPS degerini `10` yap.
5. Otomasyonu baslat ve kisa sure gozlemle.
6. Otomasyonu durdur.

Beklenen sonuc:

- 1 CPS ayarinda tiklama hizi yavas ve tutarli olur.
- 10 CPS ayarinda tiklama hizi daha hizli olur.
- Sayac sadece gerceklesen tiklamalarla artar.
- Stop sonrasi yeni tiklama uretilmez.

### M7 — Gecersiz CPS UI Davranisi

Amac:

Gecersiz CPS girislerinin UI uzerinden engellendigini veya net uyari verdigini dogrulamak.

On kosullar:

- PySide6 CPS giris alani app/domain validasyonuna baglanmis.

Adimlar:

1. CPS alanina `0` gir.
2. Start'a basmayi dene.
3. CPS alanina `101` gir.
4. Start'a basmayi dene.

Beklenen sonuc:

- Otomasyon baslamaz.
- Mesaj alani `CPS degeri 1 ile 100 arasinda olmalidir.` gosterir.
- Kullanici hangi degeri duzeltmesi gerektigini anlar.

### M8 — Yeni Calistirmada Sayac ve Sure Sifirlama

Amac:

UI uzerinde yeni run basladiginda sayac ve surenin sifirlandigini dogrulamak.

On kosullar:

- UI, AutomationService sayac ve sure bilgilerine baglanmis.

Adimlar:

1. Otomasyonu baslat.
2. Sayac veya sure ilerledikten sonra durdur.
3. Tekrar baslat.

Beklenen sonuc:

- Yeni baslangicta sayac `0` olur.
- Calisma suresi yeniden baslar.
- Onceki run degerleri yeni run'a tasinmaz.

### M9 — Pencere Secimi Opsiyonel

Amac:

Hedef pencere secilmeden otomasyonun baslatilabildigini dogrulamak.

On kosullar:

- UI hedef pencere alani uygulanmis.

Adimlar:

1. Hedef pencere secmeden uygulamayi ac.
2. Pencere korumasini kapali birak.
3. Start'a bas.

Beklenen sonuc:

- Otomasyon baslayabilir.
- Kullanici pencere secimine zorlanmaz.

### M10 — Pencere Degisince Durdurma

Amac:

Pencere korumasi acikken hedef pencere degistiginde otomasyonun guvenli durdugunu dogrulamak.

On kosullar:

- Pencere listeleme adapter'i tamamlanmis.
- Aktif pencere izleme tamamlanmis.
- Pencere korumasi UI'a baglanmis.

Adimlar:

1. Hedef pencere sec.
2. Pencere korumasini ac.
3. Otomasyonu baslat.
4. Baska pencereye gec.

Beklenen sonuc:

- Otomasyon durur.
- Mesaj alani `Pencere degisti` durma sebebini gosterir.
- Hedef pencere disinda kontrolsuz tiklama devam etmez.

### M11 — Hedef Pencere Kapanirsa Durdurma

Amac:

Hedef pencere kapanirsa otomasyonun guvenli durdugunu dogrulamak.

On kosullar:

- Pencere adapter'i hedef pencere durumunu izleyebiliyor.

Adimlar:

1. Hedef pencere sec.
2. Pencere korumasini ac.
3. Otomasyonu baslat.
4. Hedef pencereyi kapat.

Beklenen sonuc:

- Otomasyon durur.
- Mesaj alani `Hedef pencere bulunamadi` durma sebebini gosterir.

### M12 — Windows ve macOS Temel Uyumluluk

Amac:

Windows ve macOS icin ortak UI ve platform adapter ayriminin calistigini dogrulamak.

On kosullar:

- Windows adapter tamamlanmis.
- macOS adapter temel uyumluluk seviyesinde hazir.

Adimlar:

1. Uygulamayi Windows'ta ac.
2. Start / Stop, F8 ve CPS davranislarini dogrula.
3. Uygulamayi macOS'ta ac.
4. Ortak UI'nin acildigini ve platform adapter kaynakli bloklayici hata olmadigini dogrula.

Beklenen sonuc:

- Iki platformda ayni UI akisi kullanilir.
- Platforma ozel islemler adapter uzerinden ayrilir.
- macOS icin eksik implementasyon varsa kullaniciya teknik olmayan net mesaj gosterilir.

## MVP Kabul Notu

TASK-012 kapanış kontrolü sonucunda MVP'nin tam manuel kabul kararı henüz verilemez.

Bloklayıcı nedenler:

- Windows mouse backend'i gerçek OS tıklaması üretmiyor.
- Windows üzerinde gerçek uçtan uca manuel smoke test yapılmadı.

App/domain seviyesinde su davranislar dogrulanabilir durumdadir:

- CPS kurallari
- Start / Stop durum makinesi
- F8 toggle komut davranisi
- Sayac sifirlama ve basarili tiklama olayi baglantisi
- Calisma suresi
- Kullanici odakli durum ve uyari mesajlari
