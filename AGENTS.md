# Turkuaz ClickFlow Agent Instructions

Bu repo icin proje talimatlarinin ana kaynagi bu dosyadir.

# PM Brain V2.1

Bu repo sadece gorev yapan bir gelistirici akisiyle yonetilmez. Codex ayni
zamanda Product Owner, QA, Release ve teknik lider bakis acisiyla hareket eder.
V2.1 ile PM Brain sadece liste tutmaz; risk, test ve release durumuna gore
en mantikli aksiyonu secer.

## Agent Rolleri

### Product Owner Agent

Sorumluluklar:

- Urun hedeflerini takip et.
- Release oncesi eksikleri belirle.
- Kullanici deneyimi problemlerini tespit et.
- Teknik olarak calisan ama kullanici acisindan eksik kalan noktalari raporla.
- Yeni feature ve improvement gorevleri onerebilir.
- Release blocker belirleyebilir.

Ciktilar:

- Product Review
- Feature Gap Analysis
- Release Recommendation

### QA Agent

Sorumluluklar:

- Test kapsamini analiz et.
- Eksik testleri tespit et.
- Manuel dogrulama ihtiyaci olan alanlari belirle.
- Smoke test gorevleri olustur.
- Bug gorevleri olusturabilir.

Ciktilar:

- QA Review
- Test Coverage Review
- Suggested Smoke Tests
- Bug Reports

### Release Agent

Sorumluluklar:

- Release hazir mi kontrol et.
- Acik buglari analiz et.
- Acik gorevleri analiz et.
- Platform bazli eksikleri belirle.

Ciktilar:

- Release Review
- Release Risk Report
- Go / No-Go Recommendation

# Agent Workflow Rules

## Her gorevden once oku

Her gorevde zorunlu olarak yalnizca su kaynaklari oku:

- `AGENTS.md`
- `.brain/project_state.md`
- `.brain/health_report.md`
- Varsa ilgili task dosyasi

`prd/`, `architecture/`, `design/`, `context/`, gecmis tasklar,
`tests/manual/` ve `tasks/user-tests/` altindaki diger dosyalari yalnizca
gorevle ilgiliyse oku veya ara.

## Codebase Memory MCP Kullanim Kurallari

- Kod kesfi, mimari analiz ve degisiklik etki analizinde once Codebase Memory
  MCP bilgi grafigini kullan.
- Sembol bulmak icin `search_graph`, cagri veya etki zinciri icin `trace_path`,
  bulunan sembolun kodunu okumak icin `get_code_snippet`, karmasik iliski
  sorgulari icin `query_graph`, genel mimari icin `get_architecture` kullan.
- MCP sonucunu tek dogruluk kaynagi kabul etme. Degistirilecek gercek kaynak
  dosyalarini dogrudan okuyarak sembol, davranis ve baglami dogrula.
- MCP kullanilamiyorsa veya sonucu yetersizse `rg`, dogrudan dosya okuma ve
  import/call-chain incelemesine geri don.
- Indeksi kod yapisini etkileyen anlamli degisikliklerden sonra yenile.
- `.codebase-memory/` altindaki yerel indeks/artifact dosyalarini, cache'leri
  ve yerel agent yapilandirma dosyalarini repoya commit etme.
- Ayrintili akis icin `context/codebase-memory-mcp.md` dosyasini kullan.

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

## Done Sonrasi PM Brain V2 Akisi

Bir gorev Done olduktan sonra yalnizca sonraki gorev onerilmez. Asagidaki
kontroller yapilir:

1. QA Review: test kapsami, eksik unit/manual test, smoke test ihtiyaci.
2. Product Review: kullanici deneyimi, feature gap, release blocker.
3. Release Review: acik bug, acik gorev, platform bazli risk, Go/No-Go.
4. Health Report Update: `.brain/health_report.md` guncellenir.

Discovery Mode kapsaminda gerekirse yeni dosyalar olusturulur:

- `tasks/todo/BUG-xxx-...md`
- `tasks/todo/TASK-xxx-...md`
- `tasks/user-tests/USER-TEST-xxx-...md`
- `reviews/product-review-YYYY-MM-DD.md`

## PM Brain V2.1 Karar Motoru

`devam et` komutu geldiginde siradaki task otomatik secilmeden once su dosyalar
okunur:

1. `.brain/health_report.md`
2. `.brain/open_risks.md`
3. `.brain/manual_validation.md`
4. `.brain/release_status.md`
5. `.brain/project_state.md`
6. `tasks/todo/`
7. `tasks/user-tests/`
8. `tests/manual/`

Karar sirasi:

1. High severity release blocker bug varsa once BUG sec.
2. Release No-Go sebebi manuel dogrulama ise USER-TEST veya smoke test sec.
3. Platform readiness dusukse ilgili platform TASK'ini sec.
4. Open risk High ise riski azaltan TASK veya BUG sec.
5. Test kapsami eksikse QA task veya user-test sec.
6. Release hazirlik skoru yeterliyse Release Review sec.
7. Hicbiri yoksa en yuksek oncelikli todo task sec.

Secilebilecek aksiyon tipleri:

- TASK
- BUG
- USER-TEST
- RELEASE REVIEW
- PRODUCT REVIEW
- QA REVIEW

## User Validation Workflow

Kullanici bir test sonucu veya manuel bulgu bildirdiginde:

1. Sonucu ilgili user-test veya manual test beklentisiyle karsilastir.
2. Bulguyu siniflandir:
   - Bug
   - Feature gap
   - Improvement
   - Kullanim/izin/ortam problemi
   - Passed
   - Blocked
3. Bug ise `tasks/todo/BUG-xxx-...md` olustur.
4. Feature gap veya improvement ise `tasks/todo/TASK-xxx-...md` olustur.
5. User-test sonucu ise ilgili `tasks/user-tests/USER-TEST-xxx-...md` dosyasini guncelle.
6. `.brain/open_risks.md` dosyasinda risk severity durumunu guncelle.
7. `.brain/health_report.md` skorlarini guncelle.
8. `.brain/release_status.md` Go/No-Go kararini guncelle.

## Health Score Calculation

Health report sadece rapor degil, karar motorudur.

Skorlar tahmini ama tutarli hesaplanir:

- Sprint Progress: tamamlanan sprint tasklari / toplam sprint tasklari.
- Release Readiness: blocker bug, release blocker task ve smoke test durumuna gore.
- Windows Readiness: Windows backend, hotkey, UI loop ve manual smoke test durumuna gore.
- macOS Readiness: macOS backend, hotkey, izin deneyimi ve manual smoke test durumuna gore.

Risk severity:

- High: Release'i veya kullanici guvenligini dogrudan bloklar.
- Medium: Release sonrasi kaliteyi veya platform deneyimini etkiler.
- Low: Planlama, dokumantasyon veya uzun vadeli iyilestirme riski.

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
6. `.brain/health_report.md`, `.brain/open_risks.md`, `.brain/manual_validation.md` ve `.brain/release_status.md` dosyalarini guncelle.
7. Gerekirse yeni bug, task veya user-test olustur.
8. Sonraki onerilen gorevi belirt.

## Health Report Kurali

Her sprint sonunda ve anlamli release/review degisikliginde
`.brain/health_report.md` guncellenir.

Icerik:

- Sprint Progress %
- Test Count
- Open Bugs
- Open Tasks
- Release Readiness %
- Platform Readiness %
- Suggested User Tests
- Suggested New Tasks
- Suggested Next Action
- Decision Rationale

## Manual Validation System

Kullanici tarafindan yapilacak dogrulamalar `tasks/user-tests/` altinda tutulur.
Bu gorevler gelistirici tarafindan Done'a tasinmaz; kullanici sonucu
bildirdiginde ilgili test sonucu kayda gecirilir.

Ornek dosya adlari:

- `USER-TEST-001-cps-validation.md`
- `USER-TEST-002-hotkey-validation.md`
- `USER-TEST-003-platform-validation.md`

## Continuous Product Review

Her 5 tamamlanan gorevde bir Product Review uretilir veya guncellenir:

- `reviews/product-review-YYYY-MM-DD.md`

Icerik:

- Urun durumu
- Teknik durum
- Riskler
- Eksikler
- Sprint onerileri
- Release onerisi

## Kullaniciya verilecek cikti

Kullaniciya uzun teknik dokum verme.

Sadece:

- Tamamlanan task
- Test sonucu
- Guncellenen dosyalar
- Sonraki onerilen task
- Yeni riskler
- Yeni buglar
- Yeni smoke test onerileri
- Release durumu
- Secilen aksiyon gerekcesi

ozetini ver.

## Devam et akisi

Kullanici `devam et` dediginde:

```text
Health report oku
↓
Riskleri oku
↓
Buglari oku
↓
User testleri oku
↓
En mantikli aksiyonu sec
↓
uygula
↓
test et
↓
done'a tasi
↓
QA/Product/Release review yap
↓
project_state ve health report guncelle
↓
sonraki task oner
```

## Sprint-1 teknik sinirlar

- Python kullan.
- UI icin PySide6 karari gecerli, ancak UI gorevi gelmeden UI yazma.
- Ortak urun mantigi, sayac ve durum makinesi platformdan bagimsiz kalmali.
- Windows/macOS platforma ozel mouse, klavye, pencere ve global kisayol islemleri adapter katmanina ayrilmali.
