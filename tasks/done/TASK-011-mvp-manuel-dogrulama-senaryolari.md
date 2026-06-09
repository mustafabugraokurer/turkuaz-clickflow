# Kapanis Ozeti

- Durum: Done
- Tamamlanma ozeti: MVP manuel kabul senaryolari iki gruba ayrildi: su an unit/app seviyesinde dogrulanabilir senaryolar ve UI + platform adapter geldikten sonra manuel dogrulanacak senaryolar. Gercek UI ve gercek mouse tiklama olmadigi acikca belirtildi.
- Degisen dosyalar:
  - `tests/manual/mvp-acceptance-scenarios.md`
- Test sonucu: Test calistirilmadi; bu gorev sadece manuel kabul dokumani uretimidir ve kod/test kodu yazilmadi.
- Kapsam disi birakilanlar: Kod degisikligi, test kodu, PySide6 UI, mouse tiklama motoru, global hotkey OS implementasyonu, platform adapter.

# TASK-011 — MVP Manuel Doğrulama Senaryoları

## Epic

EPIC-06 — MVP Kalite ve Kabul

## Amaç

MVP'nin ürün beklentilerini karşıladığını doğrulamak için uçtan uca manuel test senaryolarını hazırlamak.

## Geliştirici Görevleri

- Start / Stop senaryosunu yaz.
- Global kısayol ile başlatma / durdurma senaryosunu yaz.
- Hız ayarı ve sayaç doğrulama senaryosunu yaz.
- Pencere hedefleme ve pencere değişince durdurma senaryosunu yaz.
- Geçersiz ayar ve hata mesajı senaryolarını yaz.

## Kabul Kriterleri

- Her MVP özelliği en az bir manuel senaryoyla doğrulanır.
- Kritik güvenlik davranışları ayrıca test edilir.
- Senaryolar ürün yöneticisinin kabul kararı vermesine yetecek açıklıktadır.

## Bağımlılıklar

- TASK-001
- TASK-003
- TASK-006
- TASK-008
- TASK-010

## Önerilen Sıra

11
