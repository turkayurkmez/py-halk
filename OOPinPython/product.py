class Product:
    """ Bir E-Ticaret uygulaması için Ürün sınıfı """
    
    name: str = None
    price: float = 1.0
    stock: int = 1

    def show_details(self):
        return f"{self.name} - {self.price} - {self.stock}"
    
    def update_price(self, new_price):
        old_price = self.price
        self.price = new_price
        print(f"{self.name} isimli ürünün yeni fiyatı {self.price} eski fiyatı ise {old_price} idi")
    
    def check_stock(self):
        if self.stock > 10:
            return "stokta var"
        elif self.stock > 0:
            return "stok kritik"
        else:
            return "Stokta yok"
    
    def test():
        print("Bu fonksiyon, sadece class içinden çağrılabilir")
