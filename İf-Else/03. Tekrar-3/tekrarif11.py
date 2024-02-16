kenar1 =   float(input("1kenar\n : "))
kenar2 =   float(input("2kenar\n : "))
kenar3 =   float(input("3kenar\n : "))  

if kenar1 == kenar2 == kenar3:
    print("Eşkenar")
elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3:
    print("İkizkenar")
else:
    print("Çeşitkenar")
