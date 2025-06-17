cities = ["Ankara","Eskişehir","Bursa","Ankara","İstanbul","İstanbul","İstanbul","Ankara","Bursa","İstanbul","Bursa","Ankara"]
city_analysis = {}
for city in cities:
    if city not in city_analysis:
        count = cities.count(city)
        city_analysis[city] = count

print(city_analysis)