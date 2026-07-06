# Packaging Strategy

## Karar Ozeti

Ilk dagitim stratejisi Windows MVP icin PyInstaller tabanli portable zip
uretmektir. Installer, portable build smoke testten gectikten sonra ayri bir
urunlestirme adimi olarak ele alinacaktir.

macOS icin PyInstaller ile `.app` bundle uretimi hedeflenir; ancak public
macOS release icin signing, notarization ve izin smoke testleri tamamlanmadan
Go karari verilmemelidir.

## Secilen Paketleme Araci

Secilen arac: PyInstaller.

Gerekce:

- Python + PySide6 masaustu uygulamalari icin tek artifact uretimini destekler.
- Windows ve macOS icin ayni temel komut modeli kullanilabilir.
- Mevcut `pyproject.toml` entry point'i `turkuaz-clickflow` olarak tanimlidir.
- Sprint-2 icin installer yerine once test edilebilir artifact uretmek daha
  dusuk risklidir.

## Windows Stratejisi

### MVP Dagitim Formu

Windows MVP icin ilk artifact portable zip olacaktir.

Artifact adi:

```text
turkuaz-clickflow-0.1.0-windows-x64-portable.zip
```

Icerik:

- PyInstaller `onedir` ciktisi
- Uygulama executable dosyasi
- PySide6 runtime dosyalari
- Kisa `README-release.txt`

### Installer Karari

Installer MVP icin release blocker degildir. Portable zip dogrulandiktan sonra
Inno Setup veya WiX tabanli installer task'i acilabilir.

Installer artifact adi:

```text
turkuaz-clickflow-0.1.0-windows-x64-setup.exe
```

## macOS Stratejisi

### Teknik Preview Formu

macOS icin ilk hedef PyInstaller `.app` bundle uretmektir.

Artifact adi:

```text
turkuaz-clickflow-0.1.0-macos-universal-preview.dmg
```

### Public Release Gereksinimleri

Public macOS release icin su kosullar tamamlanmalidir:

- Apple Developer signing kimligi belirlenmeli.
- `.app` bundle imzalanmali.
- DMG veya zip artifact notarize edilmeli.
- Accessibility ve Input Monitoring izin deneyimi manuel dogrulanmali.
- F8 global hotkey macOS uzerinde manuel dogrulanmali.

Bu kosullar tamamlanmadan macOS sadece teknik preview olarak kalir.

## Ilk Build Adimlari

### Ortak Hazirlik

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e ".[package]"
PYTHONPATH=src python3 -m unittest discover -s tests/unit
```

### Windows Portable Build

Windows ortaminda:

```bash
python -m PyInstaller --noconfirm --clean --onedir --windowed --name TurkuazClickFlow src/turkuaz_clickflow/main.py
```

Cikti:

```text
dist/TurkuazClickFlow/
```

Zip adi:

```text
turkuaz-clickflow-0.1.0-windows-x64-portable.zip
```

### macOS App Bundle

macOS ortaminda:

```bash
python3 -m PyInstaller --noconfirm --clean --windowed --name TurkuazClickFlow src/turkuaz_clickflow/main.py
```

Cikti:

```text
dist/TurkuazClickFlow.app
```

Public release oncesi signing/notarization adimlari eklenmelidir.

## Release Artifact Smoke Checklist

Her artifact icin smoke test:

1. Temiz makine veya temiz kullanici profilinde artifact acilir.
2. Uygulama UI acilir.
3. Varsayilan CPS `10` gorunur.
4. CPS `1` ile Start / Stop calisir.
5. CPS `10` ile Start / Stop calisir.
6. F8 ile durdurma calisir.
7. Sayac yalnizca gercek tiklamalarla artar.
8. Stop sonrasi yeni tiklama uremez.
9. Hedef pencere listesi acilir.
10. Hata veya izin mesaji kullanici diliyle gorunur.

Windows icin ek kontrol:

- Uygulama odakta degilken F8 durdurma calisir.

macOS icin ek kontrol:

- Accessibility izin eksiginde dogru mesaj gorunur.
- Input Monitoring izin eksiginde dogru mesaj gorunur.
- Izin verildikten sonra Start / Stop ve F8 tekrar denenir.

## Release Karari

Windows MVP:

- Portable zip smoke test Passed olursa Windows MVP release edilebilir.

macOS:

- Signing/notarization ve izin smoke testleri tamamlanmadan public release
  verilmemelidir.
