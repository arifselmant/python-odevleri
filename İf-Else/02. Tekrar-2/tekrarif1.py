import math

birinci_sinav_notu = float(input("1. notunuzu girin\n : "))
ikinci_sinav_notu = float(input("2. notunuzu girin\n : "))
performans_notu =float(input("perfonmas notunuzu girin\n : "))

Toplam = ( int(birinci_sinav_notu) + int(ikinci_sinav_notu) + int(performans_notu) )
Ortalama= ( Toplam / 3)
  

if (Ortalama > 50) :
    print("Başarili")
elif (Ortalama < 50) :   
    print("Başarisiz")