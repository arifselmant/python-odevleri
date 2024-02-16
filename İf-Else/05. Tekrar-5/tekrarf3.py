bagaj = float(input("Bagaj Ağırlığını Giriniz:"))
if bagaj <= 20:
    print("Herhangi Bir Ücret Ödemeniz Gerekmiyor")

else:
    ek_ücret = int(bagaj -20)*10

print(f"Fazla bagaj için{ek_ücret}TL Ödemelisiniz")