from functools import reduce

def get_square(x):
    return x ** 2

get_square_lambda = lambda x: x ** 2

get_total = lambda x,y: x+y

## MAP(), FILTER(), REDUCE()
## MAP()
prices = [750,1000,895,999,1500,1750]
prices_with_taxes = list(map(lambda price:price*1.20,prices))
print(list(zip(prices,prices_with_taxes)))

employees = ["hande polat","serdar eren","enis ertem"]
title_employees = list(map(lambda name: name.title(), employees))
print(title_employees)
# Filter()
more_than_1000 = list(filter(lambda price: price>1000,prices_with_taxes))
print(more_than_1000)


#çağırım örnekleri:
get_square_lambda(5)
get_total(5,6)
#get_square(5)
def include_tax(price):
    return price * 1.20 ,

customer_emails = ["ahmet@gmail.com","ayse@yahoo.com","mehmet@company.com","zeynep@outlook.com"]
company_emails = list(filter(lambda email: "company.com" in email, customer_emails))
public_email_domains = ("yahoo.com","outlook.com","gmail.com")
company_emails_alternative = list(filter(lambda email: not email.endswith(public_email_domains), customer_emails))

print(company_emails)
print(company_emails_alternative)

people =[
    {"name":"Ahmet Polat", "salary":75000, "age":42},
    {"name":"Türkay Ürkmez", "salary":65000, "age":45},
    {"name":"Bihter Ziyagil", "salary":125000, "age":30},
    {"name":"Kıvanç Tatlıtuğ", "salary":150000, "age":36}
]

for person in people:
    print(f"{person["name"]} - {person["salary"]} - {person["age"]}")

sorted_people_by_age = sorted(people,key=lambda p:p["salary"],reverse=False)
print("Sıralı liste:")
print("="*50)
for person in sorted_people_by_age:
    print(f"{person["name"]} - {person["salary"]} - {person["age"]}")

## Reduce:
numbers = [6,7,12,20,4]
multiply_all = reduce(lambda x,y: x*y,numbers)
print(multiply_all)

max_number = reduce(lambda x,y: x if x >y else y,numbers)
print(max_number)