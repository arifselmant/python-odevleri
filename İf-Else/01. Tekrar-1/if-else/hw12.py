boy =  float(input("boyunuz\n : "))
agirlik = float(input("kilonuz\n : "))
vki = agirlik / (boy * boy)

if vki < 18:
    print("Zayıf")
elif vki < 25:
    print("Normal")
elif vki < 30:
    print("Kilolu")
elif vki < 35:
    print("Obez")
else:
    print("Ciddi obez")
