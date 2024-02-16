import math 

birinci_not = float(input("1. Notunuzu Giriniz \n : "))
ikinci_not = float(input("2. Notunuzu Giriniz \n : "))
sözlü_notu = float(input("Sözlü notunuzu giriniz \n:"))

toplam = (int(birinci_not)+ int(ikinci_not)+int(sözlü_notu))
ortalama= (toplam  / 3)

if (ortalama > 50) :
    print("Başarılı")
elif (ortalama < 50) :   
    print("Başarısız")


