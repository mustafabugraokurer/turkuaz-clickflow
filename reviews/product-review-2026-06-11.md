# Product Review — 2026-06-11

## Ürün Durumu

Turkuaz ClickFlow Sprint-1 sonunda temel auto clicker deneyimine yaklaşmıştır.
Start / Stop, CPS, sayaç, süre, gerçek Windows/macOS mouse backend sınırları ve
UI ClickRunner döngüsü oluşturulmuştur.

## Teknik Durum

- Unit test sayısı: 106
- BUG-001 CPS UI reset problemi çözülmüştür.
- Windows manuel smoke test beklenmektedir.
- macOS real mouse backend vardır.
- macOS global hotkey adapter eksiktir.

## Riskler

- Windows release kararı manuel smoke test olmadan verilemez.
- macOS izin deneyimi kullanıcı açısından sürtünme yaratabilir.
- Packaging/installer olmadığı için ürün kullanıcıya dağıtılamaz.
- Ayarlar kalıcı olmadığı için tekrar kullanım deneyimi zayıf kalır.

## Eksikler

- Windows MVP Manuel Smoke Test
- macOS Global Hotkey Adapter
- Packaging / installer
- Settings persistence
- Profil sistemi
- Pencere koruması ve hedef pencere akışı

## Sprint Önerileri

1. Windows MVP smoke test tamamla.
2. macOS izin deneyimini doğrula.
3. macOS global hotkey adapter planla.
4. Packaging strategy oluştur.
5. Ayarları kaydetme görevini aç.

## PM Brain V2.1 Notu

Bir sonraki `devam et` aksiyonu sadece todo listesinden secilmemelidir.
Health report, open risks, release status ve user-test durumlari okunarak
en mantikli aksiyon secilmelidir.

Mevcut karar:

- Open bug yok.
- High severity risk: Windows smoke test eksik.
- Release status: No-Go.
- Decision engine next action: TASK-021.

## Release Önerisi

No-Go.

Windows manuel smoke test tamamlanmadan release yapılmamalıdır.
