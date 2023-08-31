from datetime import date

def calculate_age(birth_date):
    # Bugünün tarihini al
    today = date.today()
    
    # Doğum tarihini yıl, ay, ve gün olarak ayır
    birth_year, birth_month, birth_day = map(int, birth_date.split('-'))
    
    # Kullanıcının yaşını hesapla
    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
    return age

def main():
    try:
        # Kullanıcıdan doğum tarihini al
        birth_date = input("Doğum tarihinizi YYYY-AA-GG formatında girin: ")
        
        # Yaşı hesapla
        age = calculate_age(birth_date)
        
        print("Yaşınız:", age)
    except ValueError:
        print("Geçersiz tarih formatı. Lütfen YYYY-AA-GG formatında girin.")

if __name__ == "__main__":
    main()
