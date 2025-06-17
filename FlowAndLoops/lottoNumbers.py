#Sonucunda elde edeceğim şey;  1 ile 49 arasında 6 farklı rastgele sayıyı küçükten büyüğe sıralı olarak 
#içeren bir liste.

import random


lotto = []
#sadece farklı sayılar eklenmeli; yani döngünün koşulu "6'dan küçük olduğu sürece devam et" olmalı
while len(lotto) < 6:
    random_number = random.randint(1,50)
    if random_number not in lotto:
        lotto.append(random_number)

lotto = sorted(lotto)
print(lotto)
