
Başlangıç= int(input("Başlangıç sayısını girin: "))
Bitiş = int(input("Bitiş sayısını girin: "))


sonuç = 0
adet = 0
sayi = Başlangıç
while sayi <= Bitiş:
    sonuç += sayi
    adet += 1
    sayi += 1

ortalama = sonuç / adet


print("{baslangic} ile {bitis} arasındaki sayıların ortalaması: {ortalama}")