#amaç: kullanıcının girdiği 1-99 arasındaki bir sayının türkçe okunuşunu yazan kod:
# 456.789 
birler = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]

number = int(input("İki basamaklı bir sayı girin..."))
birlerBasamagi = number % 10
onlarBasamagi = number // 10

print(f"{onlar[onlarBasamagi]} {birler[birlerBasamagi]}")

