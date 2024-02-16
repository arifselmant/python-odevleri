ürün1_fiyat = int(input("1. ürünün fiyatini girin \n"))
ürün2_fiyat = int(input("2. ürünün fiyatini girin \n"))

toplam = ürün1_fiyat + ürün2_fiyat

if toplam <=200: 
      print ("ücret:",toplam )
 
elif toplam > 200:
  print ("ücret:",toplam/4)