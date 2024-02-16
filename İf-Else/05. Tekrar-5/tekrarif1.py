not1 = float(input("1.Notunuzu Giriniz :\n "))
not2 = float(input("2.Notunuzu Giriniz :\n "))
not3 = float(input("3.Notunuzu Giriniz :\n "))

Toplam = not1 + not2 + not3
Ortalama = Toplam / 3

if Ortalama > 50 :
    print("Tebrikler Sınıfı Geçtiniz")

elif Ortalama < 50 :
    print("Sınıfta Kaldınız")