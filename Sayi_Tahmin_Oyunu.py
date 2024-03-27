#Sayı Tahmin Oyunu

"""Bilgisayar 1 ile 50 arasında bir sayı tutar.Kullanıcıdan tahmin
değer istenir.Kullanıcının 10 deneme hakkı vardır..Bu uygulamada 100
üzerinden puanlama sistemi vardır.Her tahmin 10 puandır.
"""

import random
bilgisayar=random.randint(1,50)
hak=10
puan=100

for i in range(0,hak):
    tahmin = int(input("Bir tahmin değeri giriniz:"))
    if(tahmin==bilgisayar):
        print(f"Tebrikler!\n{i+1}.denemenizde doğru bildiniz.")
        puan=puan-(10*(i+1))
        print(puan,"aldınız.")
        break

    elif(bilgisayar>tahmin):
        print("Daha büyük değer girmelisiniz!")
        hak-=1

    else:
        print("Daha küçük değer girmelisiniz!")
        hak -= 1


