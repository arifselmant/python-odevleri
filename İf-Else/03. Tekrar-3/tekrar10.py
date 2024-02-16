saat = float(input("saat\n:"))

if saat <= 1:
    ücret = 5
elif 1< saat <= 5:
    ücret = saat *4
else:
    ücret = saat *3
    print(f"Ödenecek miktar : {ücret} TL")