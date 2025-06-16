number = 8
print(f"id bilgisi: {id(number)}, tip bilgisi: {type(number)}, değeri ise {number}")
number = 45
print(f"id bilgisi: {id(number)}, tip bilgisi: {type(number)}, değeri ise {number}")
name = """Python"""

print(f"id bilgisi: {id(name)}, tip bilgisi: {type(name)}, değeri ise {name}")
name = "Halkbank"
print(f"id bilgisi: {id(name)}, tip bilgisi: {type(name)}, değeri ise {name}")

print(name)

big_number = 123456789012345678901234567890
print(f"Büyük sayı tipi: {type(big_number)}, değeri: {big_number}")

some_value = None
print("some_value isimli değişkenin, ",type(some_value),id(some_value),some_value)
some_value = 'Türkay'
print("some_value isimli değişkenin, ",type(some_value),id(some_value),some_value)
some_value = 65
print("some_value isimli değişkenin, ",type(some_value),id(some_value),some_value)

some_value='Türkay'
print("some_value isimli değişkenin, ",type(some_value),id(some_value),some_value)



pi = 3.14
scientific_number = 1.5e6
print("Bilimsel gösterim:", scientific_number)
x =  27 // 4
print(x)