import random


def say_hi(name):
    return f"Merhaba  {name}"

def get_weather(city):
    return f"{city} şehrinde bugün hava {random.randint(20,35)} derece!"

def get_balance(hesap_no):
    return f"Hesapta 5000 TL var"


print("get_weather fonksiyonunun tipi:",type(get_weather),"id'si:",id(get_weather),"__name__",get_weather.__name__)

selamla = say_hi
print(selamla("Osman"))

executable_commands={
    "selam" : say_hi,
    "hava":get_weather,
    "bakiye":get_balance
}

command = input("Hangi komutu çalıştıracaksınız (selam, hava, bakiye): ")
if command in executable_commands.keys():
    if command == "selam":
        parameter = input("isminizi girin: ")
    elif command =="hava":
        parameter = input("sehir girin: ")
    elif command == "bakiye":
        parameter = input("hesap no girin: ")
    
    choosed_command = executable_commands[command]
    result_of_function = choosed_command(parameter)
    print("Sonuç:",result_of_function)

## delege olarak kullanma (fonksiyonu parametre olarak ele al)

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b != 0:
        return a/b
    return "Sıfıra bölme hatası!"


calculator = {
    "+":add,
    "-":sub,
    "*":multiply,
    "/":divide
}

num1, operator, num2 = 15, "/",3

if operator in calculator:
    processor_func = calculator[operator]
    process_result = processor_func(num1,num2)
    print(f"{num1} {operator} {num2} = {process_result}")
