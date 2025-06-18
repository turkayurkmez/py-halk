print(all([True, True, False])) # -> FALSE
numbers = [3,6,9,16]
all_of_multiply_three = all(number % 3 == 0 for number in numbers)
if all_of_multiply_three:
    print("Listenin içindeki tüm sayılar 3'ün katı")
else:
    print("...değil") 

web_crawling_criteria = {
    "isLegal":True,
    "tech_approved":False,
    "is_stable":True
}

can_i_crawl_this_site = all(web_crawling_criteria.values())
if can_i_crawl_this_site:
    print("web sitesindeki veriler çekiliyor")
else:
    print("Kriterler onaylanamadı...")

products_stock = {
    "Şort": False,
    "Bot":False,
    "Tişört":False
}

is_available_stock= any(products_stock.values())
if is_available_stock:
    print("Ürünlerden en az birinin stoğu var")
else:
    print("Ürünler stokta kalmamış")

print("Any- Herhangi biri... OR ",any([False,False,True]))
print("All- Hepsi... - And ",all([False,False,True]))

all_emails = ["turkay@","batu@gmail.com","hotmail.com"]

if any("@" in email and "." in email for email in all_emails):
    print("Eposta adreslerinden biri doğru formatta")
else:
    print("Hiçbiri doğru formatta değil!")