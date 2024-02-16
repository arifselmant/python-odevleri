tercih = "Sinema"

öğrenci_mi = True


if tercih == "sinema":
    ucret = 15
else:
    ucret = 10

if öğrenci_mi:
    ucret /= 2

print(f"Ödenecek tutar: {ucret} TL")
