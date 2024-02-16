import math 
birinci_sınav_notu = float(input("1. notunuzu girin\n : "))
ikinci_sınav_notu = float(input("2. notunuzu girin\n : "))
üçüncü_sınav_notu = float(input("3. notunuzu girin\n : "))

Toplam = ( int(birinci_sınav_notu) + int(ikinci_sınav_notu) + int(üçüncü_sınav_notu) )
ortalama= (Toplam/3)


if (ortalama > 50) :
    print("Başarılı")
elif (ortalama < 50) :   
    print("Başarısız")
