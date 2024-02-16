açı_bir = float(input("1. açıyı girin\n : "))
açı_ikinçi = float(input("2. açıyı girin\n : "))
açı_üç = float(input("3. açıyı girin\n : "))


Toplam = ( int(açı_bir) + int(açı_ikinçi) + int(açı_üç) )

if Toplam ==180 :
    print("bu bir üçgendir")
else:
    print("bu bir üçgen değildir")