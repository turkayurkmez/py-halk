import random
is_finished = False


while not is_finished:
    randomNumber = random.randint(0,100)
    is_suggestion_true = False
    while not is_suggestion_true:
        suggest = int(input("Tahmininiz nedir: "))
        if randomNumber > suggest:
            print("Yukarı")
        elif randomNumber < suggest:
            print("Aşağı")
        else:
            is_suggestion_true = True
            print("Tebrikler... Bildiniz...") 

    answer = input("Bir kez daha oynamak ister misiniz? (e/h)")
    is_finished = answer.lower() == "h"