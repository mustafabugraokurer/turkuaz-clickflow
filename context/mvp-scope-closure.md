# MVP Kapsam Kapanış Kontrolü

## Karar

MVP kabul edilmedi. Revizyon gerekli.

Sprint-1 temel mimari, domain/app kuralları, PySide6 ana pencere iskeleti,
platform adapter sınırları, ClickRunner ve Windows global hotkey adapter
katmanı oluşturuldu. Ancak ürünün "ilk kullanılabilir auto clicker" olarak
kabul edilebilmesi için gerçek tıklama üretimi ve UI üzerinden kesintisiz
çalıştırma akışı henüz tamamlanmış değildir.

## Doğrulanan Alanlar

- CPS kuralı: minimum `1`, maksimum `100`, varsayılan `10`.
- Varsayılan kısayol: `F8`.
- Start / Stop durum makinesi.
- Çalışırken tekrar Start verilince ikinci run başlatmama.
- Stop komutunun güvenli kabul edilmesi.
- Yeni run başlangıcında sayaç sıfırlama.
- Başarılı tıklama olayında sayaç artırma.
- Çalışma süresi hesaplama.
- Durum, uyarı ve durma sebebi mesajları.
- PySide6 ana pencere alanları ve viewmodel bağlantısı.
- Platform adapter arayüzleri.
- ClickRunner'ın bounded/test edilebilir tıklama adımları.
- Windows global hotkey adapter'ın backend üzerinden F8 callback routing'i.

## Bloklayıcı Eksikler

### B1 — Gerçek Windows Mouse Backend

Durum: Tamamlandı.

Windows mouse adapter için gerçek `SendInput` tabanlı backend eklenmiştir.
Windows dışı ortamda güvenli unavailable backend davranışı korunmuştur.

Kalan doğrulama:

- Gerçek OS davranışı Windows manuel smoke test ile doğrulanmalıdır.

### B2 — UI Start Akışı ClickRunner'ı Çalıştırıyor

Durum: Tamamlandı.

PySide6 Start / Stop ve OS F8 hotkey akışı `ClickLoopController` üzerinden
`ClickRunner` çalışma döngüsüne bağlanmıştır. QTimer scheduler UI event loop'u
kilitlemeden tick üretir.

Kalan doğrulama:

- Gerçek Windows ortamında uçtan uca manuel smoke test yapılmalıdır.

### B3 — Runner Arka Plan Çalışma Modeli

Durum: Tamamlandı.

ClickRunner bounded/test edilebilir yapısını korur; UI çalışma döngüsü
`ClickLoopController` ve QTimer scheduler ile sağlanır.

Kalan doğrulama:

- CPS interval davranışı Windows manuel smoke testte gözlemlenmelidir.

### B4 — Windows Üzerinde Manuel OS Doğrulama Yapılmadı

Unit testler geçmektedir, ancak gerçek Windows ortamında şu davranışlar henüz
manuel doğrulanmış değildir:

- PySide6 uygulama açılışı.
- F8'in uygulama odakta değilken yakalanması.
- Start sonrası gerçek sol tık üretimi.
- Stop/F8 sonrası tıklamanın kesilmesi.
- Kısayol kayıt hatasının kullanıcı mesajına düşmesi.

## MVP İçin Bloklayıcı Olmayanlar

- Pencere seçimi isteğe bağlıdır.
- Pencere koruması opsiyoneldir.
- macOS için gerçek mouse/global hotkey implementasyonu Sprint-1 bloklayıcısı değildir; mimari hazırlık yeterlidir.
- OCR, görüntü tanıma, makro kaydı, profil sistemi ve klavye otomasyonu kapsam dışıdır.

## Kapsam Dışı / Backlog Korunacak Maddeler

- TASK-007 — Pencere Listeleme ve Hedef Seçimi
- TASK-008 — Pencere Değişince Durdurma Davranışı
- Sağ tık / çift tık
- Makro kayıt
- Klavye otomasyonu
- OCR / görüntü tanıma
- Profil sistemi
- Dağıtım ve paketleme otomasyonu

## Önerilen Revizyon Görevleri

- TASK-021 — Windows MVP Manuel Smoke Test

## Son Test Sonucu

```bash
PYTHONPATH=src python3 -m unittest discover -s tests/unit
```

Sonuç: 92 test başarılı.

## Ürün Sahibi Kararı İçin Öneri

MVP kabul kararı verilmemeli. Önce TASK-021 tamamlanmalı. Bu görev
tamamlandıktan sonra MVP gerçek kullanım senaryosu üzerinden tekrar kapanış
kontrolüne alınmalıdır.
