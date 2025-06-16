weathers = ["Yağmurlu","Açık","Açık","Çok bulutlu","Açık"]
weather_set = set(weathers)

print(weather_set)
empty_set = set()
print(type(empty_set))
another = {}
print(type(another))


#set yani kümelerde index ile item'a ulaşamazsınız.
print(list(weather_set)[0])

A = {1,2,3,4,5}
B = {4,5,6,7,8}

print("A U B (Bileşim)",A.union(B) )
print("A n B (Kesişim)",A.intersection(B))
print("A - B ", A.difference(B))
print("A DELTA B", A.symmetric_difference(B))

C = {1,2}
print("C, A'nın alt kümesi mi?", C.issubset(A))
print("C, A'nın alt kümesi mi?", C <= A)
print("A, C'yi kapsıyor mu?", A >= C)
print("A, C'yi kapsıyor mu?", A.issuperset(C))


