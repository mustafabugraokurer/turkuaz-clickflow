# Kapanış Özeti

## Durum

Done

## Tamamlanma Özeti

macOS mouse adapter için gerçek Quartz tabanlı sol tık backend'i eklendi.
Backend mevcut mouse konumunda left down / left up event üretir, Accessibility
veya Input Monitoring izin eksikliğini güvenli şekilde `PlatformOperationError`
olarak yüzeye çıkarır. Unit testler fake Quartz API ile gerçek mouse tıklaması
üretmeden davranışı doğrular. macOS manuel smoke test notu eklendi.

## Değişen Dosyalar

- `src/turkuaz_clickflow/platform/macos/mouse.py`
- `src/turkuaz_clickflow/platform/macos/__init__.py`
- `tests/unit/test_mouse_click_adapter.py`
- `tests/unit/test_platform_interfaces.py`
- `tests/manual/macos-real-mouse-backend-smoke.md`

## Test Sonucu

```bash
PYTHONPATH=src python3 -m unittest discover -s tests/unit
```

Sonuç: 99 test başarılı.

## Kapsam Dışı Bırakılanlar

- macOS global hotkey implementasyonu
- Pencere koruması
- Paketleme / notarization
- Windows manuel smoke test

# TASK-022 — macOS Real Mouse Backend

## Epic

EPIC-02 — Tıklama Motoru ve Hız Kontrolü

## Amaç

macOS üzerinde gerçek sol tık üreten platform adapter implementasyonunu
oluşturmak.

## Not

macOS için Accessibility ve Input Monitoring izinleri gerekebilir. Bu izinler
yoksa adapter sessizce başarısız olmamalı; kullanıcıya teknik olmayan anlaşılır
bir hata/uyarı akışı üretilebilmelidir.

## Geliştirici Görevleri

- macOS sol tık işlemini platform backend'i olarak uygula.
- Mevcut platform adapter interface sınırlarını koru.
- macOS adapter'ın mouse click capability durumunu güncelle.
- İzin eksikliği ve OS çağrısı hatalarını `PlatformOperationError` ile yüzeye çıkar.
- Unit testlerde gerçek OS tıklaması üretmeden fake backend yaklaşımını kullan.
- Manuel doğrulama için macOS izin ve smoke test notu ekle.

## Kabul Kriterleri

- macOS adapter gerçek sol tık backend'i ile çalışabilir.
- Adapter app/domain iş kurallarını kopyalamaz.
- Accessibility veya Input Monitoring izni yoksa hata güvenli şekilde yüzeye çıkar.
- Unit testler gerçek mouse tıklaması üretmez.
- macOS üzerinde manuel doğrulama adımları tanımlıdır.

## Bağımlılıklar

- TASK-014
- TASK-015
- TASK-016
- TASK-020

## Kapsam Dışı

- macOS global hotkey implementasyonu
- Pencere koruması
- Paketleme / notarization
- Windows manuel smoke test

## Önerilen Sıra

22
