cift_sayilar=[6,8,10,12,14,16]

tek_sayilar=[5,7,9,11,13,15]


cift_sayilar=[6,8,10,12,14,16]

tek_sayilar=[5,7,9,11,13,15,cift_sayilar]

print(tek_sayilar)

Çıktı: [5, 7, 9, 11, 13, 15, [6, 8, 10, 12, 14, 16]]

cift_sayilar=[6,8,10,12,14,16]

tek_sayilar=[5,7,9,11,13,15]

sayilar=cift_sayilar,tek_sayilar

print(sayilar[1][1], sayilar[0][4])

Çıktı: 7;14

cift_sayilar=[6,8,10,12,14,16]

tek_sayilar=[5,7,9,11,13,15]

sayilar=tek_sayilar,cift_sayilar

print(sayilar[1][2], sayilar[1][3], sayilar[0][4])