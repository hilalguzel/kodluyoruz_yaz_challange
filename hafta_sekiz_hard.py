def armstrong_kontrol(sayi):
    toplam = 0
    basamak_sayisi = len(str(sayi))

    temp = sayi
    while temp > 0:
        basamak = temp % 10
        toplam += basamak ** basamak_sayisi
        temp //=10

        return sayi == toplam
    
sayi = int(input("Bir sayı giriniz: "))
if armstrong_kontrol(sayi):
    print(sayi, "bir armstrong sayısıdır.")
else:
    print(sayi, "bir armstrong sayısı değildir.")