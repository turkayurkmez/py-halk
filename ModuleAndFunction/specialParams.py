def get_total(*numbers):
   print("+"*100)
   return sum(numbers)

def get_avg(*n):
   total = sum(n)
   average = total / len(n)
   return average

def get_employee_profile(**kwargs):
   """ zorunlu key'ler: name, age, mail ve salary """
   for key,value in kwargs.items():
      if key == "name":
         print(f"{key.title()} {value}")
      elif key == "age":
         print(f"{key.title()} {value} yaşında") 
      elif key == "mail":
         print(f"{key.title()} {value} mail adresini kullanıyor") 
      elif key =="salary":
         print(f"{key.title()} {value} TL") 
      else:
         print(f"{key.title()}, {value}") 
    
             
            

