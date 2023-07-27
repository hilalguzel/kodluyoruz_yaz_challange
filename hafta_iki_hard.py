def calculate_profitable_quantity(unit_cost, unit_price):
    if unit_cost >= unit_price:
        return 0  # Eğer maliyet, satış fiyatından yüksekse kar edilemez.
    
    profit_per_unit = unit_price - unit_cost
    quantity_for_profit = unit_cost // profit_per_unit
    
    return quantity_for_profit

def main():
    try:
        unit_cost = float(input("Birim maliyeti girin: "))
        unit_price = float(input("Birim satış fiyatını girin: "))
        
        if unit_cost < 0 or unit_price < 0:
            print("Negatif değerler girmeyiniz.")
            return
        
        profitable_quantity = calculate_profitable_quantity(unit_cost, unit_price)
        
        print(f"Kar elde edilecek minimum ürün adedi: {profitable_quantity}")
    except ValueError:
        print("Geçersiz birim maliyet veya birim satış fiyatı. Lütfen sayısal değerler girin.")

if __name__ == "__main__":
    main()
