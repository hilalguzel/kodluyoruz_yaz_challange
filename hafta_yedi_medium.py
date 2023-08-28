sayi = int(input("Bir sayı giriniz: "))
toplam = 0

while sayi > 0:
    basamak = sayi % 10
    toplam += basamak
    sayi //= 10

print("Girmiş olduğunuz sayının basamak toplamı: ", toplam)