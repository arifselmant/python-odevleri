ürün1_fiyat = int(input("1. Ürünün fiyatını girin \n"))
ürün2_fiyat = int(input("2 . Ürünün fiyatını girin \n"))

Toplam = ürün1_fiyat + ürün2_fiyat

if Toplam <=200:
    print("Ücret: ",Toplam)

elif Toplam > 200:
  print ("ücret:",Toplam/4)
  