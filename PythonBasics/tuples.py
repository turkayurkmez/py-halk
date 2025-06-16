days = ("Pazartesi","Salı","Çarşamba","Perşembe","Cuma")
try:
    days[0] = "Pazar"
except:
    print("Tuple tipi immutable'dır değiştirilemez!")

#veri paketleyerek tuple oluşturmak:
coords = 40.32, 26.45
print("verileri paketledikten sonra tuple: ",coords)

enlem, boylam = coords
print("verileri paketten çıkardıktan sonra değerler: Enlem: ",enlem,"Boylam:",boylam)

x, y = 100,150
x, y = y,x
print(f"Atamadan sonra x: {x} ve y: {y}")

print("Pazartesi değeri demette var mı:", "Pazartesi" in days)
print("*"*60)

new_days = days * 3
print(new_days)

developer = ("Necati","Okyanus",45,["JS","Python","C#"])
