for tavuk_sayisi in range(37):
    koyun_sayisi = 36 - tavuk_sayisi
    toplam_bacak = 2 * tavuk_sayisi + 4 * koyun_sayisi
    if toplam_bacak == 100:
        print("Tavuk Sayısı:", tavuk_sayisi)
        print("Koyun Sayısı:", koyun_sayisi)
        break
