import product


if __name__ == "__main__":
    laptop = product.Product()
    laptop.name ="Dell XPS"
    laptop.price = 45000
    laptop.stock = 150
    laptop.category = "Elektronik"

 
    
    print(laptop.show_details())
    laptop.update_price(40000)
    print(laptop.check_stock())
    
    product.Product.test()