# Tasks

Bu klasor Turkuaz ClickFlow gorev yasam dongusunu tutar.

## Klasorler

- `tasks/todo/` — Baslanmamis veya siradaki gorevler
- `tasks/done/` — Tamamlanmis ve kapanis ozeti eklenmis gorevler
- `tasks/user-tests/` — Kullanici tarafindan yurutulecek dogrulama gorevleri

## Yasam Dongusu

1. Todo
2. In Progress
3. Review
4. Done

## Kapanis Kurali

Bir gorev tamamlandiginda task dosyasi `tasks/todo/` icinde kalmaz. Dosya `tasks/done/` altina tasinir ve basina kapanis ozeti eklenir.

Kapanis ozeti sunlari icermelidir:

- Durum
- Tamamlanma ozeti
- Degisen dosyalar
- Test sonucu
- Kapsam disi birakilanlar

## Guncellenmesi Gereken Dosyalar

Her tamamlanan task sonrasi:

- `context/current_sprint.md`
- `.brain/project_state.md`
- `.brain/health_report.md`
- `.brain/open_risks.md`
- `.brain/manual_validation.md`
- `.brain/release_status.md`
- `tasks/todo/README.md`
- `tasks/done/README.md`

guncellenir.

## PM Brain V2 Review Akisi

Done sonrasi su review katmanlari calisir:

1. QA Review
2. Product Review
3. Release Review
4. Health Report Update

Gerekirse yeni bug, task veya user-test dosyasi olusturulur.
