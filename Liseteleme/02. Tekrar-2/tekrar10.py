çift_sayılar = [6,8,10,12,14,16]

tek_sayılar = [5,7,9,11,13,15]

tek_sayılar=[5,7,9,11,13,15,çift_sayılar]

print(tek_sayılar)
 
Çıktı: [5, 7, 9, 11, 13, 15, [6, 8, 10, 12, 14, 16]]

çift_sayılar=[6,8,10,12,14,16]

tek_sayılar = [5,7,9,11,13,15]

sayilar=çift_sayılar,tek_sayılar

print(sayilar[1][1], sayilar[0][4])


Çıktı: 7;14

çift_sayilar=[6,8,10,12,14,16]

tek_sayilar=[5,7,9,11,13,15]

sayilar=tek_sayilar,çift_sayilar

print(sayilar[1][2], sayilar[1][3], sayilar[0][4])