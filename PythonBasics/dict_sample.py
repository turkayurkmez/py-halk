plates = {}
while True:
    plate = input("Plaka kodunu girin (çıkmak için q girin):")
    if plate.lower() == 'q':
        break
    city = input("Şehir bilgisini girin")
    if plate in plates:
        print(f"{plate} zaten daha önce eklenmiş...")
    else:
        plates[plate] = city
        print("plaka kodu eklendi")

while True:
    searchingPlate = input("aradığınız kodu girin veya çıkmak için q girin")
    if searchingPlate.lower() == 'q':
        break
    print(plates.get(searchingPlate,"Böyle bir plaka bulunamadı"))