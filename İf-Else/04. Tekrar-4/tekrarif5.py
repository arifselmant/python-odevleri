kullanıcı_adı = input("Kullanıcı adınızı giriniz: ")
sifre = int(input("Şifrenizi giriniz: "))

if kullanıcı_adı == "Türkiye"  or sifre == 1923:
    print("Giriş başarılı")
else:
    print("Kullanıcı adı ya da şifre yanlış")
