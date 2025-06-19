import product


if __name__ == "__main__":
    laptop = product.Product("Dell XPS",45000,0,"Elektronik")
    # laptop.name ="Dell XPS"
    # laptop.price = 45000
    # laptop.stock = 150
    # laptop.category = "Elektronik"

 
    
    print(laptop.show_details())
    laptop.update_price(40000)
    print(laptop.check_stock())
    
    product.Product.test()
    
    print(laptop)
    print("Repr ", repr(laptop))
    print("Len ",len(laptop))

    if laptop:
        print("Stokta var")
    else:
        print("stokta yok")

    notebook = product.Product("Lenovo",35000,0,"Elektronik")

    if laptop == notebook:
        print("İki nesne eşit")
    else:
        print("Farklı nesneler")

    if notebook < laptop:
        print(notebook, "bu ürün daha ucuz")

    if laptop>notebook:
        print("laptop pahalı...")
    
    output = max(laptop,notebook)
    print(output)

    total = laptop + notebook
    print("toplam:",total)

    laptop._features.append("32 GB Ram")
    laptop._features.append("1 TB SSD")

    if "32 GB Ram" in laptop:
        print("Bu özellik var")
    else:
        print("Bu özellik yok")

    products = [laptop,notebook]
    sorted = sorted(products)

    print(sorted)

    name = input("Ürün adı: ")
    # if len(name) < 3 :
    #     raise ValueError("Ürün adı en az üç harfli olmalı")
    
    # laptop.name = name

    laptop.name = name
    print(laptop.name)

    laptop.price = 55000

    print("güncel fiyat: ",laptop.price)




    # value = str(laptop)
    # print(value)

    #laptop.test()