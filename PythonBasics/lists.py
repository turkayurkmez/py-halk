#               0                            1     2
books = ["Denizler altında 20 bin fersah","Biz","Satranç"]

print(type(books),books)
print(books[0])

books[0]="Test"
print(type(books),books)


# List operasyonları
product_info = ["Monitör","PC", 4000, True]

numbers = [10,35,-5,45,13,100,100]
print(f"Orjinal liste: {numbers}")
numbers.append(42)
print(f"append'den sonra liste: {numbers}")
numbers.remove(100)
print(f"remove'dan sonra liste: {numbers}")
del numbers[0]
print(f"del işleminden sonra liste: {numbers}")

last_item = numbers.pop()
print("son eleman:",last_item)
print(f"pop işleminden sonra liste: {numbers}")

list1= [1,2,3]
list2= [3,4,5,6]
merged_list = list1 + list2
print("İşte birleşik liste", merged_list)

cities = ["Eskişehir", "İstanbul","Ankara","Kayseri","Bursa"]
city = input("Hangi şehri arıyordunuz? ")
if city not in cities:
    print(f"{city} şehri listede yok")
else:
    print(f"{city} şehri listede var")


refCopy = cities

refCopy.append("Erzurum")
print("Orijinal liste:", cities)

contentCopy = cities.copy()
contentCopy.append("Tunceli")
print("Orijinal liste:", cities)
print("İçeriği copy() ile kopyalanan liste:",contentCopy)

#slicing:
print("Son eleman:",cities[-1])
print("İlk üç eleman:",cities[0:3])
print("İlk üç eleman:",cities[:3])
print("Son üç eleman:",cities[-3:])
print("İlk 1 ve 2. indeksteki elemanlar:",cities[1:3])
print("2'şer ilerleme", cities[::2])




