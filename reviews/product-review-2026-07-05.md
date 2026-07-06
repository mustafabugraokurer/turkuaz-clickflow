# Product Review - 2026-07-05

## Urun Durumu

Turkuaz ClickFlow Windows MVP icin release candidate seviyesine geldi. Temel
kullanici vaadi olan kontrollu sol tiklama, CPS ayari, Start / Stop, F8 ile
durdurma, sayac ve calisma suresi akislari dogrulandi.

## Teknik Durum

- Unit test paketi 146 test ile basarili.
- Windows real mouse backend ve global hotkey akisi manuel smoke testten gecti.
- Pencere listeleme ve hedef secimi eklendi.
- macOS real mouse backend ve global hotkey adapter unit test seviyesinde var.

## Riskler

- macOS global hotkey manuel dogrulamasi cross-platform release icin bekliyor.
- macOS izin mesajlari netlestirildi; manuel dogrulama bekliyor.
- Packaging stratejisi belirlendi; artifact uretimi ve smoke test bekliyor.
- Ayarlar kalici hale getirildi; yeniden acilis manuel smoke testi bekliyor.

## Eksikler

- macOS permission smoke test.
- macOS F8 hotkey manuel smoke test.
- Release artifact smoke test.
- Settings persistence manuel smoke test.
- Pencere degisince durdurma manuel smoke test.

## Sprint Onerileri

1. QA Review.
2. Window guard smoke test.
3. Settings persistence smoke test.
4. Release artifact smoke test.

## Release Onerisi

Windows MVP: Go.

Cross-platform public release: No-Go. macOS hotkey/izin manuel dogrulamasi,
artifact smoke test ve macOS signing/notarization tamamlanmadan genel release
karari verilmemelidir.
