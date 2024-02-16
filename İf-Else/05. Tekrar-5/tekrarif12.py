boy = float(input("Boyunuz \n:"))

ağırlık = float(input("Ağırlığınızı Giriniz \n:"))

vkı = ağırlık / (boy * boy)

if vkı < 18:
    print("Zayıf")

elif vkı < 25:
    print("Normal")

elif vkı <30:
    print("Kilolu")

elif vkı < 35:
    print("Obez")
else:
    print("Ciddi Obez")