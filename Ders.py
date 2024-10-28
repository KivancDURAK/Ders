import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" 
giris = int(input("Parolanızın karakter sayısını giriniz"))
sifre = ""
for i in range (giris):
    sifre += random.choice(karakterler)
print(sifre)
