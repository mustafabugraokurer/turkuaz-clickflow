# Kapanış Özeti

## Durum

Done

## Tamamlanma Özeti

CPS değerinin UI refresh sırasında varsayılan `10` değerine dönmesi düzeltildi.
ViewModel artık kullanıcı tarafından seçilen CPS değerini ayrı state olarak
tutar. UI refresh snapshot'ı bu seçimi korur, Start seçili CPS ile çalışır ve
Stop sonrası değer yeni run için korunur.

## Değişen Dosyalar

- `src/turkuaz_clickflow/ui/viewmodels/main_window_viewmodel.py`
- `src/turkuaz_clickflow/ui/views/main_window.py`
- `tests/unit/test_main_window_viewmodel.py`

## Test Sonucu

```bash
PYTHONPATH=src python3 -m unittest discover -s tests/unit
```

Sonuç: 106 test başarılı.

## Kapsam Dışı Bırakılanlar

- Ayarları uygulama kapanışı sonrası kalıcı kaydetme
- Profil sistemi
- UI tasarım değişikliği

# BUG-001 — CPS değeri UI'da 10'a geri dönüyor

## Tür

Release bloklayıcı bug

## Bulgular

Gerçek manuel testte aşağıdaki davranışlar doğrulandı:

- Start çalışıyor.
- Stop çalışıyor.
- Gerçek mouse tıklama çalışıyor.
- Süre ilerliyor.
- CPS `10` ile doğru çalışıyor.

Ancak CPS artırılınca veya azaltılınca UI değeri tekrar `10` değerine dönüyor.
Kullanıcının seçtiği CPS korunmuyor.

## Beklenen Davranış

- Kullanıcı CPS değerini değiştirdiğinde seçilen değer UI'da korunmalı.
- Start sonrası otomasyon seçilen CPS ile çalışmalı.
- UI refresh sırasında CPS alanı domain varsayılanı olan `10` değerine geri dönmemeli.

## Olası Etki

- Kullanıcı 1-100 CPS aralığını pratikte güvenilir şekilde kullanamaz.
- MVP hız ayarı kabul kriteri tam karşılanmaz.
- Release kararı verilmemelidir.

## Kabul Kriterleri

- CPS alanında kullanıcı seçimi korunur.
- Start sonrası snapshot/refresh CPS değerini kullanıcı seçimine göre gösterir.
- Stop sonrası CPS değeri korunur.
- Yeni run başlatılırken seçilen CPS kullanılır.
- Unit test veya uygun app/viewmodel testi eklenir.

## Kapsam Dışı

- Ayarları uygulama kapanışı sonrası kalıcı kaydetme
- Profil sistemi
- UI tasarım değişikliği

## Öncelik

P0 — Release bloklayıcı
