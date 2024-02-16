import math

birinci_sınav_notu = float(input("1. notunuzu girin\n : "))
ikinci_sınav_notu = float(input("2. notunuzu girin\n : "))
performans_notu =float(input("perfonmas notunuzu girin\n : "))

Toplam = ( int(birinci_sınav_notu) + int(ikinci_sınav_notu) + int(performans_notu) )
Ortalama= ( Toplam / 3)
  

if (Ortalama > 50) :
    print("Başarılı")
elif (Ortalama < 50) :   
    print("Başarısız")


