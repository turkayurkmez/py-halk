
try:
    kilo = int(input("Lütfen kilonuzu girin "))
    boy = float(input("Boyunuzu metre olarak girin "))

    vki = kilo / (boy ** 2)

    print("VKİ değeriniz: ",  vki)
except ValueError:
    print("Lütfen sayısal değerler girdiğinize ve ondalık ayıracı olarak (.) kullandığınıza emin olun ")

if vki < 25:
    print("Her şey yolunda")
elif vki > 26 and vki <= 29.9:
    print("Şişman...")
else: 
    print("Obez....")
  