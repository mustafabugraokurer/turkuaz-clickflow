# Todo Tasks

Bu klasor henuz tamamlanmamis gorevleri tutar.

## Siradaki Onerilen Gorev

TASK-021 — Windows MVP Manuel Smoke Test

## Decision Engine Notu

`devam et` komutu geldiginde siradaki aksiyon sadece bu listeye gore secilmez.
Once `.brain/health_report.md`, `.brain/open_risks.md`,
`.brain/release_status.md`, `.brain/manual_validation.md` ve
`tasks/user-tests/` okunur.

Mevcut karar:

- Acik bug yok.
- High severity risk: Windows smoke test eksik.
- Release status: No-Go.
- En mantikli aksiyon: TASK-021.

## Sprint-1 Todo

- TASK-001 — MVP Kabul Cercevesini Netlestir
- TASK-021 — Windows MVP Manuel Smoke Test

## Sprint-1 Disi / Opsiyonel

- TASK-007 — Pencere Listeleme ve Hedef Secimi
- TASK-008 — Pencere Degisince Durdurma Davranisi

## Bagimlilik Notlari

- TASK-001 erken planlama gorevi olarak kalmistir; MVP kapanis kontrolu TASK-012 ile guncel durum uzerinden yapilmistir.
- TASK-021, MVP kabulunun mevcut bloklayicisidir ve Windows uzerinde calistirilmalidir.
- Mevcut ortam `darwin` oldugu icin TASK-021 henuz tamamlanamaz; Windows manuel smoke test sonucu beklenmektedir.

## User Test Notlari

Kullanici tarafindan yurutulecek dogrulamalar `tasks/user-tests/` altindadir:

- USER-TEST-001 — CPS Validation
- USER-TEST-002 — Hotkey Validation
- USER-TEST-003 — Platform Validation
