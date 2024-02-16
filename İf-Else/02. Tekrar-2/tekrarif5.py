kullanici_adi = input("Kullanici adinizi giriniz: ")
sifre = int(input("Şifrenizi giriniz: "))

if kullanici_adi == "Türkiye"  or sifre == 1923:
    print("Giriş başarili")
else:
    print("Kullanici adi ya da şifre yanliş")
