total_all = lambda *args: sum(args)
print(total_all(4,12,-1))

max_number = lambda *args: max(args) if args else None
result = max_number(-5,0,16,-2,24)
if result:
    print("En büyük sayı",result)
else:
    print("Koleksiyonda sayı yok ya da boş...")

calculator = lambda **kwargs: {
    "total": sum(value for value in kwargs.values() if isinstance(value, (int,float))),
    "count": len([v for v in kwargs.values() if isinstance(v, (int,float))]),
    "average": sum(value for value in kwargs.values() if isinstance(value, (int,float)))/
               len([v for v in kwargs.values() if isinstance(v, (int,float))])
               if len([v for v in kwargs.values() if isinstance(v, (int,float))]) > 0 else 0
}

operational_result = calculator(ocak=15000, subat=25000, mart=22500)
print(operational_result)