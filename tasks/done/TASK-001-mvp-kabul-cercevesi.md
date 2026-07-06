# Durum

Tamamlandi.

# Tamamlanma Ozeti

MVP kabul cercevesi Sprint-1 sonunda guncel dogrulama sonuclariyla netlestirildi.
TASK-012 kapsam kapanis kontrolu, TASK-021 Windows MVP manuel smoke test sonucu
ve 2026-07-05 release review birlikte degerlendirildi.

Son karar:

- Windows MVP kabul kriterleri saglandi.
- Windows MVP release candidate icin Go.
- macOS teknik preview seviyesinde; cross-platform public release icin No-Go.
- V2+ ve Sprint-2 kapsaminda kalacak maddeler backlog/task olarak ayrildi.

# Degisen Dosyalar

- `context/mvp-scope-closure.md`
- `context/current_sprint.md`
- `.brain/health_report.md`
- `.brain/project_state.md`
- `.brain/release_status.md`
- `.brain/manual_validation.md`
- `tasks/todo/README.md`
- `tasks/done/README.md`

# Test Sonucu

```bash
PYTHONPATH=src python3 -m unittest discover -s tests/unit
```

Sonuc: 118 test basarili.

# Kapsam Disi Birakilanlar

- macOS global hotkey adapter implementasyonu TASK-024 ile daha sonra tamamlandi.
- macOS izin smoke testinin kullanici tarafinda yurutulmesi
- Packaging artifact uretimi ve smoke test
- Ayar kaliciligi TASK-026 ile daha sonra tamamlandi.
- Pencere degisince durdurma davranisi

# TASK-001 - MVP Kabul Cercevesini Netlestir

## Epic

EPIC-06 - MVP Kalite ve Kabul

## Amac

MVP'nin hangi davranislarla tamam sayilacagini urun, gelistirme ve test
acisindan netlestirmek.

## Kabul Edilen MVP Cercevesi

Windows MVP icin olmazsa olmaz kabul listesi:

- Masaustu uygulamasi acilir.
- CPS 1-100 araliginda calisir; varsayilan CPS 10'dur.
- Start / Stop butonlari otomasyonu kontrol eder.
- Varsayilan global kisayol `F8` ile durdurma calisir.
- Sol tik otomasyonu gercek Windows ortaminda tiklama uretir.
- Stop veya F8 sonrasi tiklama kesilir.
- Sayac yalnizca gerceklesen tiklamalarla artar.
- Calisma suresi gorunur.
- Gecersiz ayarlarla baslatma engellenir veya kullaniciya net mesaj verilir.

## MVP Disi / Backlog

- macOS global hotkey manuel dogrulamasi
- macOS izin deneyimi iyilestirmesi TASK-027 ile daha sonra tamamlandi.
- Packaging artifact uretimi ve smoke test
- Settings persistence
- Pencere degisince durdurma davranisi
- Sag tik / cift tik
- Makro kaydi
- Profil sistemi
- OCR / goruntu tanima

## Dogrulama Kaynaklari

- `tests/manual/windows-mvp-smoke-test-result.md`
- `tasks/done/TASK-021-windows-mvp-manuel-smoke-test.md`
- `context/sprint-1-release-review.md`
- `.brain/release_status.md`

## Sonraki Onerilen Aksiyon

TASK-025 - Packaging Strategy
