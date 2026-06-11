# Windows MVP Manuel Smoke Test Sonucu

## Durum

Yürütülemedi.

## Sebep

Bu test gerçek Windows ortamı gerektirir. Mevcut çalışma ortamı Windows değildir.

```text
sys.platform: darwin
```

Bu nedenle aşağıdaki kabul kriterleri bu makinede doğrulanamaz:

- Uygulamanın Windows üzerinde açılması.
- Start sonrası gerçek Windows `SendInput` sol tık üretimi.
- F8 global kısayolunun uygulama odakta değilken çalışması.
- Stop veya F8 sonrası gerçek tıklamanın kesilmesi.
- Sayaç değerinin yalnızca gerçekleşen gerçek tıklamalarla artması.

## Hazır Test Senaryosu

Windows ortamında çalıştırıldığında aşağıdaki adımlar uygulanmalıdır.

1. Windows üzerinde proje bağımlılıklarını kur.
2. Uygulamayı başlat.
3. Güvenli ve boş bir hedef alan aç.
4. CPS değerini `1` yap.
5. Start butonuna bas.
6. Gerçek sol tık üretimini ve sayaç artışını gözlemle.
7. Stop butonuna bas.
8. Stop sonrası yeni tıklama üretilmediğini doğrula.
9. CPS değerini `10` yap.
10. F8 ile otomasyonu başlat.
11. Uygulamayı arka plana al.
12. F8 ile otomasyonu durdur.
13. Durma sebebinin `F8 ile durduruldu` olarak göründüğünü doğrula.

## Beklenen Sonuç

- Uygulama Windows üzerinde açılır.
- Start gerçek tıklama üretir.
- Stop ve F8 güvenli şekilde durdurur.
- Sayaç yalnızca gerçekleşen tıklamalarla artar.
- Kritik bloklayıcı hata kalmaz.

## Ürün Kararı

TASK-021 tamamlanmış sayılmamalıdır. Windows ortamında manuel smoke test
çalıştırılana kadar MVP kabul kararı verilmemelidir.
