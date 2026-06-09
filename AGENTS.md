# Turkuaz ClickFlow Agent Instructions

Bu repo icin proje talimatlarinin ana kaynagi bu dosyadir.

# Agent Workflow Rules

## Her gorevden once oku

- `prd/`
- `.brain/`
- `architecture/`
- `design/`
- `context/`
- `tasks/`

## Temel davranis

- Mevcut urun kararlarini ve sprint kapsamlarini dikkate al.
- Kullanici ozellikle istemedikce kapsam disi teknoloji, UI veya platform kodu ekleme.
- Urun kodu degistiriyorsan ilgili unit testleri ekle veya guncelle.
- Task tamamlanmadan final cevap verme.

## Gorev yasam dongusu

### Todo

Henuz baslanmamis veya siradaki is olarak bekleyen gorevler `tasks/todo/` altinda durur.

### In Progress

Aktif calisilan gorevdir. Ayrica klasor tasimasi gerekmez; calisma sirasinda task dosyasi `tasks/todo/` altinda kalabilir.

### Review

Kod veya dokuman degisikligi tamamlanmis, test/dogrulama ve kapsam kontrolu yapilmaktadir.

### Done

Kabul kriterleri tamamlanmis, test sonucu veya dogrulama notu yazilmis gorevdir. Done gorevleri `tasks/done/` altinda tutulur.

## Gorev tamamlama kurallari

Bir gorev tamamlandiginda asla `tasks/todo/` icinde birakma.

Tamamlanan gorev icin:

1. Task dosyasini `tasks/done/` icine tasi.
2. Dosyanin basina sunlari ekle:
   - Durum
   - Tamamlanma ozeti
   - Degisen dosyalar
   - Test sonucu
   - Kapsam disi birakilanlar
3. `context/current_sprint.md` dosyasini guncelle.
4. `.brain/project_state.md` dosyasini guncelle.
5. `tasks/todo/README.md` ve `tasks/done/README.md` dosyalarini guncelle.
6. Sonraki onerilen gorevi belirt.

## Kullaniciya verilecek cikti

Kullaniciya uzun teknik dokum verme.

Sadece:

- Tamamlanan task
- Test sonucu
- Guncellenen dosyalar
- Sonraki onerilen task

ozetini ver.

## Devam et akisi

Kullanici `devam et` dediginde:

```text
TASK sec
↓
uygula
↓
test et
↓
done'a tasi
↓
project_state guncelle
↓
sonraki task oner
```

## Sprint-1 teknik sinirlar

- Python kullan.
- UI icin PySide6 karari gecerli, ancak UI gorevi gelmeden UI yazma.
- Ortak urun mantigi, sayac ve durum makinesi platformdan bagimsiz kalmali.
- Windows/macOS platforma ozel mouse, klavye, pencere ve global kisayol islemleri adapter katmanina ayrilmali.

