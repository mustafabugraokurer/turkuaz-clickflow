# Codebase Memory MCP Entegrasyonu

## Amac

Codebase Memory MCP, Turkuaz ClickFlow icin kod kesfi, mimari analiz ve
degisiklik etki analizinin ilk aracidir. Bilgi grafigi hizli yon bulma saglar;
gercek kaynak kodun yerine gecmez.

## Standart Akis

1. Sembol veya kavrami `search_graph` ile bul.
2. Cagiranlari, cagrilanlari veya etki alanini `trace_path` ile incele.
3. Gerekirse `query_graph` ile karmasik iliskileri veya `get_architecture` ile
   genel yapisal gorunumu sorgula.
4. `get_code_snippet` ile hedef sembolun kodunu incele.
5. Degistirilecek gercek kaynak dosyalarini dogrudan oku; MCP bulgularini
   dosyadaki guncel kod, importlar ve testlerle dogrula.
6. MCP kullanilamiyorsa veya kapsam yetersizse `rg`, dogrudan dosya okuma ve
   import/call-chain incelemesini kullan.

## Indeksleme ve Yenileme

- MCP proje adi: `turkuaz-clickflow`
- Repository kokunu `index_repository` ile indeksle.
- Kapsamli ilk indeks veya buyuk yapisal degisiklikte `full`, daha hizli ara
  guncellemelerde ihtiyaca uygun `moderate` veya `fast` modunu kullan.
- Kod yapisini, importlari, cagri zincirlerini veya mimariyi etkileyen anlamli
  degisikliklerden sonra indeksi yenile.
- Indeks sonrasi `get_architecture` veya hedefli bir `search_graph` sorgusuyla
  grafigin okunabildigini dogrula.

## Dogruluk ve Guvenlik Siniri

- Bilgi grafigi gecikmis, eksik veya yanlis eslesmis olabilir.
- Bir degisiklik karari yalnizca MCP sonucuna dayandirilmaz.
- Degistirilecek kaynak dosya ve ilgili testler her zaman dogrudan okunur.
- String literal, config, dokumantasyon ve kod disi dosya aramalarinda dogrudan
  `rg` veya dosya okuma kullanilabilir.

## Repository Hijyeni

- `.codebase-memory/` yerel indeks, artifact ve cache alanidir; `.gitignore`
  kapsamindadir ve commit edilmez.
- Yerel MCP cache'leri ve yerel agent yapilandirma dosyalari commit edilmez.
- Paylasilabilir proje kurallari `AGENTS.md` ve bu dokumanda tutulur.

