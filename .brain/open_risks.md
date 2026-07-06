# Open Risks

## RISK-002 - macOS Global Hotkey Eksik

Durum: Azaltildi

Severity: Low

Etki:

- macOS release iddiasi icin F8 global kisayolun gercek OS davranisi manuel
  dogrulanmali.

Azaltma:

- TASK-024 macOS Global Hotkey Adapter tamamlandi.
- USER-TEST-002 macOS hotkey retest bekliyor.

## RISK-003 - macOS Izin Deneyimi Belirsiz

Durum: Azaltildi

Severity: Low

Etki:

- Accessibility veya Input Monitoring izni yoksa kullanici artik hedef izin
  turune yonlendirilir; gercek macOS smoke test sonucu beklenir.

Azaltma:

- TASK-027 macOS Permission UX Review tamamlandi.
- USER-TEST-004 macOS Permission Validation beklemede.

## RISK-004 - Packaging / Installer Yok

Durum: Azaltildi

Severity: Low

Etki:

- Packaging stratejisi var; gercek artifact uretimi ve smoke test henuz
  yapilmadi.

Azaltma:

- TASK-025 Packaging Strategy tamamlandi.
- Release artifact smoke test bekliyor.

## RISK-005 - Ayarlar Kalici Degil

Durum: Kapandi

Severity: Low

Etki:

- CPS, hotkey, hedef pencere ve pencere koruma ayarlari JSON config ile
  saklanir.

Azaltma:

- TASK-026 Settings Persistence tamamlandi.

## RISK-006 - Pencere Koruma Manuel Dogrulama Bekliyor

Durum: Azaltildi

Severity: Low

Etki:

- Pencere degisince durdurma davranisi unit test seviyesinde var; gercek OS
  pencere degisimi manuel dogrulanmalidir.

Azaltma:

- TASK-008 Pencere Degisince Durdurma Davranisi tamamlandi.
- `tests/manual/window-guard-smoke.md` eklendi.
