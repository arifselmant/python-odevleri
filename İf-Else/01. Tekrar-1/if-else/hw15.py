tercih = "sinema"  
ogrenci_mi = True  

if tercih == "sinema":
    ucret = 15
else:
    ucret = 10

if ogrenci_mi:
    ucret /= 2

print(f"Ödenecek tutar: {ucret} TL")
