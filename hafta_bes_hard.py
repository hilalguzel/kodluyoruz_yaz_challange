import math

try:
    sayi = float(input("Lütfen bir sayı giriniz: "))
    karakok = math.sqrt(sayi)

    if karakok == int(karakok):
        print(f"{sayi} 'nin karekökü, {int(karakok)}'dır")

    else:
        print(f"{sayi}'nin karekökü tam olarak çıkmaz.")

except ValueError:
    print("Geçersiz sayı girdiniz")