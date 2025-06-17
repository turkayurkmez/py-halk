language = "Python"
for letter in language:
    print(letter)

for number in range(1,10):
    result ="Çift" if number % 2 == 0 else "Tek"
    #result = number % 2 == 0 ? "Çift" : "Tek"
    print(number,result)

participants = ["Leyla Akyol","Çağrı Karadeniz","Banu Çaykara","Efe Küçük"]
for order,participant in enumerate(participants,1):
    print(f"{order}. -> {participant}")

names = ["Enes","Hakan","Mehmet Enis"]
ages = [30,25,28]
cities = ["İstanbul","Ankara","İzmir"]

mergedList = list(zip(names,ages,cities))
for order, value in enumerate(mergedList,100):
    print(f"{order}. {value[0]} isimli katılımcı, {value[1]} yaşında ve {value[2]} şehrinde yaşıyor")


for number in range(1,100):
    if number % 2 == 0:
        pass
        print("Hiç bir şey yapmadık")
    else:
        print("Tek sayı")

#pass: Eğer sonradan düzeltilecek bir iş varsa algoritmaya zarar vermemesi için "pass" keywordü kullanılabilir.