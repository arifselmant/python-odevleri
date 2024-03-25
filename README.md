# Arif Selman Telli 
## İf-Else Ödev1
# Proje1
## 1)  Kullanıcıdan iki sınav ve bir performans notu girmesini isteyiniz. Girilen 3 notun ortalaması 50 ve daha büyükse “Başarılı”; değilse “Başarısız” çıktıları veren kodu yazınız.
````python
import math

birinci_sınav_notu = float(input("1. notunuzu girin\n : "))
ikinci_sınav_notu = float(input("2. notunuzu girin\n : "))
performans_notu =float(input("perfonmas notunuzu girin\n : "))

Toplam = ( int(birinci_sınav_notu) + int(ikinci_sınav_notu) + int(performans_notu) )
Ortalama= ( Toplam / 3)
  

if (Ortalama > 50) :
    print("Başarılı")
elif (Ortalama < 50) :   
    print("Başarısız")

````

# Proje2
##  Bir üçgenin iç açıları toplamı 180 derecedir. Kullanıcının girdiği üç açı değerine göre “Bu bir üçgendir.” ya da “Bu bir üçgen değildir.” çıktıları veren kodu yazınız.
````python

açı_bir = float(input("1. açıyı girin\n : "))
açı_ikinçi = float(input("2. açıyı girin\n : "))
açı_üç = float(input("3. açıyı girin\n : "))


Toplam = ( int(açı_bir) + int(açı_ikinçi) + int(açı_üç) )

if Toplam ==180 :
    print("bu bir üçgendir")
else:
    print("bu bir üçgen değildir")

````

# Proje3
## Bir hava yolu firması en fazla 20 kilogram bagaj hakkı vermektedir. 20 kilogramdan sonraki her kilogram için 10 TL ek ücret almaktadır. Buna göre bagajı 20 kg ya da daha az olan yolculara “Herhangi bir ücret ödemeniz gerekmiyor.”; 20 kg’den fazla olanlar için de ne kadar ek ücret ödeneceğini hesaplayarak “Fazla bagaj için ….. TL ödemelisiniz.” çıktılarını veren kodu yazınız. 
Not: Bu soruda kilogram hesabında sadece tam sayıları dikkate alınız. Örneğin 28,70 kilogram olan bagaj için sadece 8 kg için ek ücret ödenmesi yeterlidir.

 ````python
bagaj = float(input("Bagajın ağırlığını giriniz: "))
if bagaj <= 20:
    print("Herhangi bir ücret ödemeniz gerekmiyor.")
else:
    ek_ucret = int(bagaj -20 ) * 10
    print("Fazla bagaj için {ek_ucret} TL ödemelisiniz.")

````

# Proje4
## Kullanıcının girdiği iki ürünün toplam fiyatı 200 TL ve altıysa “Ödenecek miktar=…. TL”; 200 TL’yi geçerse %25 indirim yaparak “Ödenecek miktar, indirimden sonra ….. TL’dir.” çıktılarını veren kodu yazınız.

````python4
ürün1_fiyat = int(input("1. ürünün fiyatını girin: \n"))

ürün2_fiyat = int(input("2. ürünün fiyatını girin: \n"))

toplam = ürün1_fiyat + ürün2_fiyat

if toplam <= 200:
    print("Ücret: ",toplam)

elif toplam > 200:
  print ("ücret:",toplam)

````

# Proje5
## Kullanıcıdan kullanıcı adı ve şifre girilmesi istensin. Kullanıcı adı “Türkiye”; şifre 1923 ise “Giriş başarılı”; değilse “Kullanıcı adı ya da şifre yanlış” çıktıları veren kodu yazınız
````python
kullanici_adı = input("Kullanıcı adınızı giriniz: ")
sifre = int(input("Şifrenizi giriniz: "))

if kullanici_adı == "Türkiye"  or sifre == 1923:
    print("Giriş başarılı")
else:
    print("Kullanıcı adı ya da şifre yanlış")
````
# Proje6
## Girilen sayı hem 3 hem de 5’e tam bölünüyorsa “15’e tam bölünür.”; bölünmüyorsa “15’e tam bölünmez.” çıktıları veren kodu yazınız.
````python

if sayi % 3 == 0 or sayi % 5 == 0:
    print("15'e tam bölünür.")
else:
    print("15'e tam bölünmez.")

````

# Proje7
##  Bir programın bilgisayara kurulması için i7 işlemci ya da en az 8 GB RAM belleğe ihtiyaç duyulmaktadır. Şartlar sağlanıyorsa “Kurulum uygun”; sağlanmıyorsa “Kurulum uygun değil” çıktıları veren programı yazınız.

````python
islemci = 'i5'
ram = 8

mesaj = "Kurulum uygun" if islemci == 'i7' or ram >= 8 else "Kurulum uygun değil"
print(mesaj)
````
# Proje8
## Girilen plaka kodu 06 ise ekrana Ankara, 07 ise Antalya, 08 ise Artvin, bunların dışında girilen tüm değerlerde ise Türkiye çıktısı veren kodu yazınız
````python
plaka_kodu = 67

if plaka_kodu == 67:
    print("Zongludak")

elif plaka_kodu == 81:
    print("Düzce")

elif plaka_kodu == 69:
    print("Bayburt")

else:
    print("Türkiye")

````
# Proje9
## Kullanıcı tarafından girilen hava sıcaklığı 5 °C ve altındaysa “Soğuk”; 6-14 °C arasındaysa “Ilık”; 15 °C ve daha fazlaysa “Sıcak” çıktılarını veren kodu yazınız. 
````python
sıcaklık = float(input("Sıcaklık \n"))

if sıcaklık <=5:
    print("Soğuk")

elif 6<= sıcaklık >= 14:
    print("Ilık")

else:
    ("Sıcak")
````
# Proje10
## Kullanıcı tarafından girilen hava sıcaklığı 5 °C ve altındaysa “Soğuk”; 6-14 °C arasındaysa “Ilık”; 15 °C ve daha fazlaysa “Sıcak” çıktılarını veren kodu yazınız.

````python
saat = float(input("Saat \n :"))

if saat <=1:
    ücret = 5

elif 1 < saat <= 5:
    ücret = saat * 4
else:
    ücret = saat * 3

print(f"Ödenecek miktar: {ücret} TL")
````
# Proje11
## Üçgenler kenar uzunluklarına göre üçe ayrılmaktadır: Eşkenar, İkizkenar ve Çeşitkenar. Kullanıcının girdiği 3 kenar uzunluğuna göre üçgenin türünü ekrana yazdırınız.
````python
açı1 = float(input("Birinci açıyı giriniz: \n"))

açı2= float(input("İkinci açıyı giriniz: \n"))

açı3 = float(input("Üçüncü açıyı giriniz: \n"))

if açı1 == açı2 == açı3:
    print("Bu Bir Eşkenar Üçgendir ")

elif açı1 == açı2 or açı1 == açı3:
    print("Bu Bir ikizkenar üçgendir")

else:
    print("Bu bir çeşitkenar üçgendir"
````
# Proje12
## Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini  (VKİ=ağırlık/(boy*boy), boy metre cinsinden verilmeli) hesaplayınız. VKİ 18 ile < 25 aralığındaysa normal, VKİ 25 ile <30 aralığındaysa kilolu, VKİ 30 ve daha yüksekse obez, VKİ 35 ve daha fazlaysa ciddi obez olarak kabul edilir. VKİ’ni hesaplayarak kişinin durumunu yazdırınız.
````python
boy = float(input("Boyunuz \n:"))

ağırlık = float(input("Ağırlığınızı Giriniz \n:"))

vkı = ağırlık / (boy * boy)

if vkı < 18:
    print("Zayıf")

elif vkı < 25:
    print("Normal")

elif vkı <30:
    print("Kilolu")

elif vkı < 35:
    print("Obez")
else:
    print("Ciddi Obez")
````
# Proje13
## Kullanıcıdan adını, maaşını ve çalışma yılını girmesini isteyiniz. 0-5 yıl arası çalışanlara %10; 6-10 yıl arası çalışanlara %15; 11 ve daha fazla yıl çalışanlara %25 zam yapılmaktadır. Buna göre “Sayın …………….., zamlı maaşınız …….. TL” çıktısı veren kodu yazınız.
````python
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
````
# Proje14
## Girilen üç sayıdan en büyüğünü bulan kodu yazınız.
````python
sayi1 = 357475454745714144417414741
sayi2 = 444444444477848478788112509
sayi3 = 100000454485847874988554545

en_buyuk = max(sayi1, sayi2, sayi3)
print(f"En büyük sayı: {en_buyuk}")
````
# Proje 15
## Kullanıcıya sinema ya da tiyatro tercihi sorulsun. Sinema izlemek için 15 TL, tiyatro için 10 TL ödenmesi gerekmedir. Öğrencilere %50 indirim yapıldığı düşünülerek öğrenci ise indirim yapılan; öğrenci değilse indirimsiz tutarı hesaplayarak ekrana yazdıran kodu yazınız
````python
tercih = "Sinema"

öğrenci_mi = True


if tercih == "sinema":
    ucret = 15
else:
    ucret = 10

if öğrenci_mi:
    ucret /= 2

print(f"Ödenecek tutar: {ucret} TL")
````
----------------------------------------------------------------------------------------------
# Listeleme Ödev 1
# Proje1
##  Elemanları haftanın günleri olan bir liste oluşturunuz ve ekrana yazdırınız.
````python
haftanin_günleri=["PAZARTESİ","SALI","ÇARŞAMBA","PERŞEMBE","CUMA","CUMARTESİ","PAZAR"]
print(haftanin_günleri)
````
# Proje2
##  En sevdiğiniz 3 şeyi liste hâline getirerek ekrana yazdırınız
```python
Futbolcular = ["Sergen","Arda","Tuncay"]
print(Futbolcular)
````
# Proje 4
## Haftanın günlerinden Pazartesi ile başlayan ve Cuma ile biten bir liste oluşturunuz. Oluşturduğunuz listenin indeksi 4 olan elemanını ekrana yazdırınız
`````python
 gunler =["pazartesi","salı","çarşamba","perşembe","cuma","cumartesi","pazar"]

print(gunler)
``````
# Proje 5
## Aşağıdaki kod nasıl bir çıktı üretir? asal_sayilar=[2, 3, 5, 7, 11, 13, 17, 19, 23] print(asal_sayilar[::2])
````python

asal_sayilar=[2, 3, 5, 7, 11, 13, 17, 19, 23]
 
print(asal_sayilar[::2]) 
````
# Proje 6
## Elemanları sırasıyla sanat, sanat, içindir olan listeyi sanat, toplum, içindir şeklinde değiştiriniz
````python
liste = ["sanat", "sanat", "içindir"]


liste[1] = "toplum"


print(liste)
````
# Proje 7
## Değerleri sırasıyla 3,1,2 olan listeyi 1,1,2 olarak değiştiriniz.
````python
liste = [3, 1, 2]

liste[0] = 1
liste[1] = 1

print(liste)
````
# Proje 8
## Adı ders, elemanları sırasıyla B,İ,L,İ,Ş,İ,M olan bir liste oluşturarak aşağıdaki işlemleri yapınız. a)  Listeyi alfabetik olarak sıralayınız. b)  Listeyi tersten yazdırınız. c)  Listede kaç tane İ elemanı olduğunu bulunuz. ç) Gerekli harfleri silerek listeyi B,İ,L,İ,M hâline getiriniz. d) ders listesini alan listesine kopyalayarak ekrana alan listesini yazdırınız. e) Listenin tüm elemanlarını siliniz. f) L elemanının indeksini bulunuz. 
````python
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
````
# Proje 9
## Adı sayilar, elemanları sırasıyla 35, 26, 81, 64 olan bir liste oluşturarak aşağıdaki işlemleri yapınız. a)  Listeyi büyükten küçüğe doğru sıralayınız. b)  Listeyi tersten yazdırınız. c)  Listede kaç tane 26 elemanı olduğunu bulunuz. ç) Listedeki 81 sayısını siliniz. d) Listenin tüm elemanlarını siliniz. e) 64 elemanının indeksini bulunuz.f) Listeyi ondalikli_sayilar isimli, elemanları 1.4, 6.8 olan liste ile birleştiriniz
````python
    sayilar = [35, 26, 81, 64]
print("Örnek Liste :{0}".format(sayilar))
 
sayilar.sort(reverse=True)
print("Yeni Liste  :{0}".format(sayilar))



sayilar = [35, 26, 81, 64]
print("Örnek Liste :{0}".format(sayilar))
 
sayilar.reverse()
print("Yeni Liste  :{0}".format(sayilar))




sayilar = [35, 26, 81, 64]
print("Örnek Liste :{0}".format(sayilar))
 
 
adet = sayilar.count(26)
 
print("26 Sayısı {0} Tanedir".format(adet))


sayilar = [35, 26, 81, 64]
print("Örnek Liste :{0}".format(sayilar))
 
sayilar.remove(81)
print("Yeni Liste  :{0}".format(sayilar))



sayilar = [35, 26, 81, 64]
print("Örnek Liste :{0}".format(sayilar))
 
sayilar.clear()
print("Yeni Liste  :{0}".format(sayilar))


sayilar = [35, 26, 81, 64]
print("Örnek Liste :{0}".format(sayilar))
 
 
sayilar = [35, 26, 81, 64]
print("Örnek Liste :{0}".format(sayilar))
 
 
sayilar.remove(64)
print("Yeni Liste  :{}".format(sayilar))




sayilar = [35, 26, 81, 64]
print("Örnek Liste :{0}".format(sayilar))
 
ondalikli_sayilar=[ 1.4, 6.8]
sayilar.extend(ondalikli_sayilar)
 
print("Yeni Liste  :{0}".format(sayilar))
 ````
# Proje 10
## 5 ile 15 (15 dâhil) arasındaki tek sayıları bir listeye alınız. 6 ile 16 (16 dâhil) arasındaki çift sayıları da başka bir listeye alınız. a)  Oluşturduğunuz tek sayılar listesine çift sayıları ekleyerek iç içe bir liste hazırlayınız. b)  Ekran çıktısı olarak 7 14 üreten kodu yazınız. c)  Ekrana sırasıyla çift sayılar listesinden 10 ve 12; tek sayılar listesinden 13 yazdırınız

````python
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
````
# Proje 11
## Aşağıdaki sözlükleri oluşturarak sizlerden istenen işlemleri yapınız. sozluk = {“Bilim insanı”:”Aziz Sancar”, “Şair”:”Mehmet Akif Ersoy”, “Astronom”:”Ali Kuşçu” } a)  sozluk isimli sözlüğü meslekler isimli başka bir sözlüğe kopyalayınız ve ekrana yazdırınız. a)  sozluk isimli sözlüğü meslekler isimli başka bir sözlüğe kopyalayınız ve ekrana yazdırınız. b)  sozluk isimli sözlüğün değerlerini ekrana yazdırınız. c)  sozluk isimli sözlüğü içi boş bir sözlük hâline getiriniz. ç) sozluk isimli sözlüğe Matematikçi: Cahit Arf ikilisini ekleyiniz. d) sozluk isimli sözlüğün içinde sanatçı anahtarının olup olmadığını sorgulayınız. e) sozluk isimli sözlüğün bilim insanı anahtarındaki değeri Canan Dağdeviren olarak değiştiriniz.f) sozluk isimli sözlüğün şair anahtarı ile eşleşen değeri ekrana yazdırınız.
````python
sözlük = {"Bilim insanı":"Aziz Sancar","Şair":"Mehmet Akif Ersoy","Astronom":"Ali Kuşçu"}
  

meslek = sözlük.copy()
print(meslek)

sozluk = {"Bilim insanı":"Aziz Sancar", "Şair":"Mehmet Akif Ersoy", "Astronom":"Ali Kuşçu" }

print(sözlük.values())

sozluk = {"Bilim insanı":"Aziz Sancar", "Şair":"Mehmet Akif Ersoy", "Astronom":"Ali Kuşçu" }
sözlük.clear()
print(sözlük)


sozluk = {"Bilim insanı":"Aziz Sancar", "Şair":"Mehmet Akif Ersoy", "Astronom":"Ali Kuşçu" }
sözlük["Matematikçi"] = "Cahit Arf"
print(sözlük)


sozluk = {"Bilim insanı":"Aziz Sancar", "Şair":"Mehmet Akif Ersoy", "Astronom":"Ali Kuşçu" }

print(sozluk.get("Sanatçı"))


sozluk = {"Bilim insanı":"Aziz Sancar", "Şair":"Mehmet Akif Ersoy", "Astronom":"Ali Kuşçu" }
 
sozluk["Bilim insanı"]="Canan Dağdeviren"


sozluk = {"Bilim insanı":"Aziz Sancar", "Şair":"Mehmet Akif Ersoy", "Astronom":"Ali Kuşçu" }
 
print(sozluk["Şair"])

````
# Proje 12
##  onemli_telefonlar = {“Acil Çağrı Merkezi”:”112”, “Polis İmdat”:”155”, “Milli Eğitim Bakanlığı İletişim Merkezi”:”444 0 632” } a)  önemli_bilgiler isimli sözlüğün değerlerini ekrana yazdırınız. b)  önemli_bilgiler isimli sözlüğü siliniz. c)  önemli_bilgiler isimli sözlükten Acil Çağrı Merkezi anahtarını ve değerini siliniz. d) önemli_bilgiler isimli sözlükte Sağlık Bakanlığı İletişim Merkezi olup olmadığını sorgulayınız. e) önemli_bilgiler isimli sözlüğü içi boş bir sözlük hâline getirini

````python
onemli_bilgiler = {"Acil Çağrı Merkezi":"112", "Polis İmdat":"155", "Milli Eğitim Bakanlığı İletişim Merkezi":"444 0 632" }
 
print(onemli_bilgiler.values())


 
onemli_bilgiler = {"Acil Çağrı Merkezi":"112", "Polis İmdat":"155", "Milli Eğitim Bakanlığı İletişim Merkezi":"444 0 632" }
 
print(onemli_bilgiler)


onemli_bilgiler = {"Acil Çağrı Merkezi":"112", "Polis İmdat":"155", "Milli Eğitim Bakanlığı İletişim Merkezi":"444 0 632" }
 
onemli_bilgiler.pop("Acil Çağrı Merkezi")
 
print(onemli_bilgiler)


 
onemli_bilgiler = {"Acil Çağrı Merkezi":"112", "Polis İmdat":"155", "Milli Eğitim Bakanlığı İletişim Merkezi":"444 0 632" }
 
durum = onemli_bilgiler.get("Sağlık Bakanlığı İletişim Merkezi")
 
print(durum)



onemli_bilgiler = {"Acil Çağrı Merkezi":"112", "Polis İmdat":"155", "Milli Eğitim Bakanlığı İletişim Merkezi":"444 0 632" }
 
onemli_bilgiler.clear()
 
print(onemli_bilgiler)


````
----------------------------------------------------------------------------------------------------------------------
# While Ödev 1
# Proje1
##  1-30 (30 dâhil) arasındaki tek sayıları while döngüsü ile ekrana yazdırınız.

````python
sayi = 1 
while sayi<=30:
    print(sayi)
    sayi+=2
````
# Proje 2
## 60-30 (30 dâhil değil) arasındaki çift sayıları azalan sırada while döngüsü ile ekrana yazdırınız. 

````python
sayi = 60

while sayi > 30:
    if sayi % 2 == 0:
        print(sayi)
    sayi -= 2
````
# Proje 3
##  0-100 (100 dâhil) arasındaki sayılardan 5’e tam bölünenleri while döngüsü ile ekrana yazdırınız.
````python
sayi = 0

while sayi <= 100:
    if sayi % 5 == 0:
        print(sayi)
    sayi += 1
````
# Proje 4
## Ekran çıktısı aşağıdaki gibi olan kodu while döngüsü ile yazınız. 1 . sınıf , 2. sınıf , 3. sınıf.......12.sınıf
````python
sinif = 1

while sinif <= 12:
    print(f"{sinif}. sınıf")
    sinif += 1
````

# Proje 6
## Girilen iki sayı arasındaki sayıları toplayan programı while döngüsü ile yazınız. 

````python

sayı1=int(input("Başlangıcı giriniz : "))
sayı2=int(input("Bitişi giriniz : "))
toplam=0
i = sayı1
while i <= sayı1:
  toplam+=i
  i += 1
print(toplam)


````

# Proje 7
 ## Girilen 2 sayı arasındaki sayıların ortalamasını bulan bir programı while döngüsü şle yazınız 
 ````python

baslangic = int(input("Başlangıç sayısını girin: "))
bitis = int(input("Bitiş sayısını girin: "))


toplam = 0
adet = 0
sayi = baslangic
while sayi <= bitis:
    toplam += sayi
    adet += 1
    sayi += 1

ortalama = toplam / adet


print("{baslangic} ile {bitis} arasındaki sayıların ortalaması: {ortalama}")

````
# Proje 8
## 20 ile 50 arasındaki (50 dahil) çift sayıları toplamını bulan programı ehile döngüsü ile yazınız
````python
sayi = 20
toplam = 0

while sayi <= 50:
    if sayi % 2 == 0:
        toplam += sayi
    sayi += 1

print("20 ile 50 arasındaki çift sayıların toplamı:", toplam)
````
# Proje 9
## Klavyeden 1 girilene kadar girilen sayıların ortalamasını alan kodu yazınız 
````python
toplam = 0
i = 0
sayi = 1234  

while sayi != 1:
    sayi = int(input("Bir sayı giriniz: "))
    i += 1
    toplam += sayi

ortalama = toplam / (i - 1)
print("Sayıların ortalaması {ortalama}")
````

# Proje 10
## Girilen şifre "Python" olana kadar "Tekrar Deneyiniz" uyarısı veren , "Python" girildiğinde "Giriş Başarılı" uyarısını veren kkodu yazınız
````python
dogru_sifre = "Python"

while input("Şifre: ") != dogru_sifre:
    print("Tekrar deneyiniz.")

print("Giriş başarılı.")

 ````







 
















