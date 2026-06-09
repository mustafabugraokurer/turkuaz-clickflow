# Tasks

Bu klasor Turkuaz ClickFlow gorev yasam dongusunu tutar.

## Klasorler

- `tasks/todo/` — Baslanmamis veya siradaki gorevler
- `tasks/done/` — Tamamlanmis ve kapanis ozeti eklenmis gorevler

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
- `tasks/todo/README.md`
- `tasks/done/README.md`

guncellenir.

