# MVP Kapsam Kapanis Kontrolu

## Karar

Windows MVP kabul edildi.

Sprint-1 sonunda temel mimari, domain/app kurallari, PySide6 ana pencere,
platform adapter sinirlari, ClickRunner, Windows real mouse backend, Windows
global hotkey adapter ve UI calisma dongusu tamamlandi. Windows uzerinde
yapilan manuel smoke test Passed sonuc verdi.

Genel cross-platform public release henuz hazir degildir. macOS tarafi teknik
preview seviyesindedir.

## Kabul Edilen Windows MVP Davranislari

- Uygulama Windows uzerinde acilir.
- CPS kuralı: minimum `1`, maksimum `100`, varsayilan `10`.
- Start / Stop butonlari otomasyonu kontrol eder.
- Varsayilan global kisayol `F8` ile durdurma calisir.
- Start sonrasi gercek Windows sol tik uretimi yapilir.
- Stop veya `F8` sonrasi tiklama kesilir.
- `1` CPS ve `10` CPS manuel olarak dogrulanmistir.
- Sayac gerceklesen tiklamalarla artar.
- Calisma suresi gorunur.
- Hedef pencere listeleme ve secimi vardir.
- Gecersiz CPS kullaniciya anlasilir mesaj olarak yansitilir.

## Dogrulanan Alanlar

- CPS araligi ve varsayilan deger.
- Varsayilan kısayol: `F8`.
- Start / Stop durum makinesi.
- Calisirken tekrar Start verilince ikinci run baslatmama.
- Stop komutunun guvenli kabul edilmesi.
- Yeni run baslangicinda sayac sifirlama.
- Basarili tiklama olayinda sayac artirma.
- Calisma suresi hesaplama.
- Durum, uyari ve durma sebebi mesajlari.
- PySide6 ana pencere ve viewmodel baglantisi.
- UI Start / Stop ve F8 akisi ile ClickRunner calisma dongusu.
- Windows `SendInput` tabanli real mouse backend.
- Windows global hotkey adapter.
- Pencere listeleme ve hedef secimi.
- macOS Quartz mouse backend.

## MVP Icin Bloklayici Olmayanlar

- Pencere degisince durdurma davranisi Sprint-2 guvenlik/kontrol iyilestirmesidir.
- macOS global hotkey adapter unit test seviyesinde vardir; cross-platform
  release icin gercek macOS ortaminda dogrulanmalidir.
- macOS Accessibility/Input Monitoring izin mesajlari netlestirildi; gercek
  macOS ortaminda manuel dogrulanmalidir.
- Packaging stratejisi vardir; artifact uretimi ve smoke test Windows MVP
  dagitimi icin gereklidir.
- Settings persistence TASK-026 ile tamamlandi; manuel yeniden acilis smoke testi
  bekliyor.

## Kapsam Disi / Backlog Korunacak Maddeler

- Sag tik / cift tik
- Makro kaydi
- Klavye otomasyonu
- OCR / goruntu tanima
- Profil sistemi

## Son Test Sonucu

```bash
PYTHONPATH=src python3 -m unittest discover -s tests/unit
```

Sonuc: 146 test basarili.

## Manuel Dogrulama Sonucu

Windows MVP manuel smoke test Passed:

- `1` CPS tiklama calisti.
- `10` CPS tiklama calisti.
- `Start` / `Stop` akisi calisti.
- `F8 ile durduruldu` davranisi retest sonrasi calisti.

## Urun Sahibi Karari

Windows MVP release candidate icin Go.

Cross-platform public release icin No-Go; macOS global hotkey, macOS izin
deneyimi ve packaging/signing/notarization isleri tamamlanmalidir.
