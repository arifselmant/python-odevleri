açı_bir = float(input("1. Açıyı Giriniz \n:"))
açı_iki = float(input("2. Açıyı Giriniz \n:"))
açı_üç = float(input("2. Açıyı Giriniz \n:"))
 
Toplam = (int(açı_bir)+int(açı_iki) + int(açı_üç))
 
if Toplam == 180:
 print("Bu Bir Üçgendir")
else:
 print("Bu Bir Üçgen Değildir")