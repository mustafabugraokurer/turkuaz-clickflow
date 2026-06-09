# Önerilen Dosya Ağacı

Bu dosya ağacı Sprint-1 görevleri, DEC-005 platform adapter kararı ve DEC-006 Python + PySide6 teknoloji kararı dikkate alınarak oluşturulmuştur.

```text
turkuaz-clickflow/
├── architecture/
│   ├── README.md
│   ├── file-tree.md
│   ├── layered-architecture.md
│   └── modules.md
├── context/
│   ├── current_focus.md
│   ├── current_sprint.md
│   └── sprint-1-output.md
├── epics/
├── prd/
│   └── business_prd.md
├── src/
│   └── turkuaz_clickflow/
│       ├── app/
│       ├── config/
│       ├── domain/
│       ├── platform/
│       │   ├── macos/
│       │   └── windows/
│       └── ui/
│           ├── viewmodels/
│           └── views/
├── tasks/
│   ├── done/
│   └── todo/
└── tests/
    ├── integration/
    ├── manual/
    └── unit/
```

## Sprint-1 Minimum Modül Önceliği

1. `domain` — CPS kuralları, sayaç, durum ve durma sebebi
2. `platform` — Windows adapter öncelikli, macOS adapter sınırı hazır
3. `app` — Start / Stop, tıklama döngüsü ve kısayol orkestrasyonu
4. `ui` — PySide6 ana yüzey ve kullanıcı geri bildirimleri
5. `tests` — Domain kuralları, uygulama akışı ve manuel kabul senaryoları

## Kod Yazımına Geçmeden Önce Kabul

- PySide6 UI katmanı, uygulama/domain katmanından ayrıdır.
- Windows ve macOS adapter klasörleri görünürdür.
- Ortak ürün mantığı platform klasörlerinin dışında kalır.
- Sprint-1 Windows odaklıdır, ancak macOS uyumluluk hazırlığı mimari ağaçta yer alır.

