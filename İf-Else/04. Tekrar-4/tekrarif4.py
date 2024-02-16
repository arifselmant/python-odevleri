ürün1_fiyat = float(input("1. Ürünün Fiyatını Giriniz: \n"))
ürün2_fiyat = float(input("2. Ürünün Fiyatını Giriniz: \n"))

toplam = ürün1_fiyat + ürün2_fiyat

if toplam <= 200:
    print("Ücret:",toplam)


elif toplam > 200:
  print ("ücret:",toplam)