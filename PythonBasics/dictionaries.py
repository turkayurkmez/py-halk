film = {
    "title":"Matrix",
    "director":"Wachowski's Brothers",
    "year":1999,
    "actors":["Neo", "Morpheus", "Trinitiy","Ajan Smith"],
    "imdb":8.0
}

print(type(film),film)

print(film["title"],film["year"])
print(film.get("genre","Yok"))
print("genre key'i var mı? ", "genre" in film)

film["year"] = 2000

print("Keys koleksiyonu:",film.keys())
print("Values koleksiyonu:",film.values())
print("Items koleksiyonu:",film.items())

for key, value in film.items():
    print(f"Anahtar: {key}, Değer: {value}")

users = {
    "turkayurkmez":{
        "name":"Türkay",
        "lastname":"Ürkmez",
        "age":45,
        "email":"turkay.urkmez@gmail.com",
        "address":{
            "city":"Eskişehir",
            "state":"Odunpazarı"
        }


    }
}

print("ilk kullanıcının yaşadığı ilçe:",users["turkayurkmez"]["address"]["state"])