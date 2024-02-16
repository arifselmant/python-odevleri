toplam = 0
i = 0
sayi = 1234  

while sayi != 1:
    sayi = int(input("Bir sayı giriniz: "))
    i += 1
    toplam += sayi

ortalama = toplam / (i - 1)
print("Sayıların ortalaması {ortalama}")
