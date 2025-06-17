import mathFunc
import optionalParameter
import specialParams
from hangman import hangman 



if __name__ == "__main__":    
    print("Bu uygulamanın ilk çalışan kısmı olacak")
    mathFunc.showModuleName()
    total = mathFunc.add(7,8)
    diff = mathFunc.sub(12,4)

    ##hangman()

    result =  optionalParameter.getArea(a=5)
    print(result)
    result =  optionalParameter.getArea(a=5, shape="daire")

    print(result)
    result =  optionalParameter.getArea(a=5,b=3,shape="üçgen")
    print(result)

    print(specialParams.get_total(8,-1,12,124,70))
    print(specialParams.get_avg(100,85,80,90))
    print(specialParams.get_employee_profile(name="Türkay",age=45,mail="a@b.com",salary=80000,department="HR"))







# Bir dosya içerisindeki __name__ değişkeninin değeri eğer "__main__" ise bu 
# uygulamanın o dosyadan ayağa kalktığını, eğer dosya adı ("mathFunc") dönüyorsa
# Bu başka bir dosyaya import edildiğini gösterir.