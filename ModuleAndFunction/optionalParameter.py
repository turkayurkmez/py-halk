import math


def getArea(a, b=1,shape="kare"):
    if shape.lower() == "kare":
        return a**2
    elif shape.lower() == "daire":
        return math.pi * (a**2)
    elif shape.lower() == "üçgen":
        return (a*b)/2
    elif shape.lower() == "dikdörtgen":
        return (a*b)
    else:
        print(f"{shape} diye bir tanım yok!")
        return 1








 