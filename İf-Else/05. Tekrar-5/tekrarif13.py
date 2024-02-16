ad ="Arif"
maaş = 13000
çalışma_yılı = 5

if çalışma_yılı <= 5:
    zamlı_maaş = maaş *1.10

elif çalışma_yılı <= 10:
    zamlı_maaş = maaş *1.15

else:
    zamlı_maaş = maaş * 1.25

print(f"Sayın {ad}, zamlı maaşınız {zamlı_maaş} TL")
