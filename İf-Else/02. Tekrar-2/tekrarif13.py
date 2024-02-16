isim = "Arif"  
maas = 3000  
calisma_yili = 6  

if calisma_yili <= 5:
    zamli_maas = maas * 1.10
elif calisma_yili <= 10:
    zamli_maas = maas * 1.15
else:
    zamli_maas = maas * 1.25

print(f"Sayın {isim}, zamlı maaşınız {zamli_maas} TL")
