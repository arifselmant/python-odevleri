açı1 = float(input("Birinci açıyı giriniz: \n"))

açı2= float(input("İkinci açıyı giriniz: \n"))

açı3 = float(input("Üçüncü açıyı giriniz: \n"))

if açı1 == açı2 == açı3:
    print("Bu Bir Eşkenar Üçgendir ")

elif açı1 == açı2 or açı1 == açı3:
    print("Bu Bir ikizkenar üçgendir")

else:
    print("Bu bir çeşitkenar üçgendir")