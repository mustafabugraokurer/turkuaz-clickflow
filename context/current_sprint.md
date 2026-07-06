# Sprint 2

## Amac

macOS readiness, izin deneyimi ve urunlesme hazirligini ilerletmek.

## Sprint-1 Kapanis Durumu

### Done

- BUG-001 - CPS UI Reset
- BUG-002 - Windows F8 ile durdurma calismiyor
- TASK-001 - MVP Kabul Cercevesini Netlestir
- TASK-002 - Ana Yuzey Bilgi Mimarisi
- TASK-003 - Hiz Ayari Kurallari
- TASK-004 - Sol Tiklama Motoru, domain temeli kismi tamamlandi
- TASK-005 - Start / Stop Durum Makinesi
- TASK-006 - Global Kisayol Baslat / Durdur Akisi
- TASK-007 - Pencere Listeleme ve Hedef Secimi
- TASK-008 - Pencere Degisince Durdurma Davranisi
- TASK-009 - Sayac ve Calisma Suresi
- TASK-010 - Durum, Uyari ve Durma Sebebi Mesajlari
- TASK-011 - MVP Manuel Dogrulama Senaryolari
- TASK-012 - MVP Kapsam Kapanis Kontrolu
- TASK-013 - PySide6 Ana Pencere MVP
- TASK-014 - Platform Adapter Interface
- TASK-015 - Mouse Click Adapter
- TASK-016 - Click Runner
- TASK-017 - UI ile AutomationService Baglantisi
- TASK-018 - OS Global Hotkey Adapter
- TASK-019 - Windows Real Mouse Backend
- TASK-020 - UI ClickRunner Calisma Dongusu Baglantisi
- TASK-021 - Windows MVP Manuel Smoke Test
- TASK-022 - macOS Real Mouse Backend

### Sprint-1 Todo

Yok.

## Sprint-2 Durumu

### Done

- TASK-024 - macOS Global Hotkey Adapter
- TASK-025 - Packaging Strategy
- TASK-026 - Settings Persistence
- TASK-027 - macOS Permission UX Review

### Todo

Yok.

### Sonraki Onerilen Task

USER-TEST-006 - Window Guard Validation

### MVP Kapanis Notu

Windows MVP smoke testi Passed sonuc verdi. `Start` / `Stop`, `1` CPS, `10`
CPS ve `F8` ile durdurma akisi dogrulandi.

Windows MVP icin ana blokajlar kapandi. macOS tarafi teknik preview
seviyesinde kalmaya devam ediyor.

### Release Review Notu

2026-07-05 tarihinde release review guncellendi. Windows MVP icin Go, genel
cross-platform public release icin macOS hotkey, izin deneyimi ve packaging
eksikleri nedeniyle No-Go karari korundu.

### Sprint-1 Kapanis Notu

TASK-001 kapatildi. Sprint-1 icin kalan planlama kalintisi yok.

### Sprint-2 Platform Notu

TASK-024 tamamlandi. macOS global hotkey adapter unit test seviyesinde
dogrulandi; gercek macOS izin ve F8 smoke testleri kullanici dogrulamasi
bekliyor.

### Sprint-2 Izin UX Notu

TASK-027 tamamlandi. macOS mouse izin hatalari Accessibility, hotkey izin
hatalari Input Monitoring mesajina yonlendiriliyor. Gercek macOS izin smoke
testi kullanici dogrulamasi bekliyor.

### Sprint-2 Packaging Notu

TASK-025 tamamlandi. Windows MVP icin PyInstaller portable zip stratejisi
secildi; macOS icin `.app` bundle, signing ve notarization gereksinimleri
dokumante edildi.

### Sprint-2 Settings Notu

TASK-026 tamamlandi. CPS, hotkey, hedef pencere ve pencere koruma tercihleri
JSON config ile kalici hale getirildi; bozuk config durumunda varsayilanlara
guvenli donus var.

### Window Guard Notu

TASK-008 tamamlandi. Pencere korumasi acikken hedef pencere degisir veya
bulunamazsa otomasyon tiklama gondermeden durur.

### QA Review Notu

2026-07-06 QA Review tamamlandi. Blocker bug bulunmadi. Yeni kullanici
dogrulamalari: settings persistence, window guard ve release artifact smoke.
