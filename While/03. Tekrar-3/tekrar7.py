
baslangic = int(input("Başlangıç sayısını girin: "))
bitis = int(input("Bitiş sayısını girin: "))


toplam = 0
adet = 0
sayi = baslangic
while sayi <= bitis:
    toplam += sayi
    adet += 1
    sayi += 1

ortalama = toplam / adet


print("{baslangic} ile {bitis} arasındaki sayıların ortalaması: {ortalama}")
