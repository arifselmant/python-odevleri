ders=['B','İ','L','İ','Ş','İ','M']
print("Liste      :{}".format(ders))


ders.reverse()
print("Yeni Liste :{}".format(ders))


 
adet = ders.count("İ")
print("Listede {} tane İ vardır".format(adet))

ders=['B','İ','L','İ','Ş','İ','M']
print("Liste      :{}".format(ders))
 
ders.pop(4)
print("Yeni Liste :{}".format(ders))    

ders=['B','İ','L','İ','Ş','İ','M']
print("Liste      :{}".format(ders))
 
ders.clear()
print("Yeni Liste :{}".format(ders))

ders=['B','İ','L','İ','Ş','İ','M']
print("Liste      :{}".format(ders))
 
ilk_sira = ders.index('L')
print("L İlk Sıra :{}".format(ilk_sira))
