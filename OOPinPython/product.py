import datetime


class Product:
    """ Bir E-Ticaret uygulaması için Ürün sınıfı """
    
    # name: str = None
    # _price: float = 1.0
    # _stock: int = 1
    _features:list = []

    def __init__(self, name, _price,_stock,_category):
        self._name =name
        self._price = _price
        self._stock = _stock
        self._category = _category
        self._price_history = [_price]
        self._updated_date = datetime.datetime.now()
        print("instance oluşturuldu")


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name:str):
        if not isinstance(new_name,str) or len(new_name)< 3:
            raise ValueError("Ürün adı en az 3 harfli olmalı")
        
        old_name = self._name
        self._name = new_name
        print(f"{old_name} olan isim {new_name} olarak güncdellendi")
        self._updated_date = datetime.datetime.now()
        print(self._updated_date)

    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, (int,float)) or new_price <= 0:
            raise ValueError("fiyat pozitif sayı olmalı")
        
        old_price = self._price
        self._price = new_price
        self._price_history.append(new_price)

        change_rate = ((new_price-old_price)/old_price) * 100
        if change_rate > 0:
            print(f"{self._name} fiyatı, %{change_rate} artarak {new_price} oldu ")
        else:
            print(f"{self._name} fiyatı, %{change_rate} azalarak {new_price} oldu ")

        
        print("Ürün fiyat geçmişi: ",self._price_history)

        self._updated_date = datetime.datetime.now()



    
    def __str__(self):
        return f"{self._name} isimli ürünün fiyatı {self._price} TL'dir ve stokta {self._stock} adet vardır. Ayrıca kategorisi {self._category} olarak belirtilmiştir"

    def __repr__(self):
        return f"Product(name:{self.name}, price:{self._price}, stock:{self._stock}, category:{self._category})"    
    
    def __len__(self):
        return self._stock
    
    def __bool__(self):
        return self._stock > 0
    
    def __eq__(self, value):
        return self._name == value.name and self._price == value._price
    
    def __lt__(self, value):
        return self._price < value._price
    
    def __gt__(self,value):
        return self._price > value._price
    
    def __add__(self, value):
        return self._price + value._price
    
    def __contains__(self,item):
        return item in self._features

    

    def show_details(self):
        return f"{self._name} - {self._price} - {self._stock}"
    
    def update_price(self, new_price):
        old_price = self._price
        self._price = new_price
        print(f"{self._name} isimli ürünün yeni fiyatı {self._price} eski fiyatı ise {old_price} idi")
    
    def check_stock(self):
        if self._stock > 10:
            return "stokta var"
        elif self._stock > 0:
            return "stok kritik"
        else:
            return "Stokta yok"
    
    def test():
        print("Bu fonksiyon, sadece class içinden çağrılabilir")

    
