bagaj = float(input("Bagajın ağırlığını giriniz: "))
if bagaj <= 20:
    print("Herhangi bir ücret ödemeniz gerekmiyor.")
else:
    ek_ucret = int(bagaj -20 ) * 10
    print("Fazla bagaj için {ek_ucret} TL ödemelisiniz.")
