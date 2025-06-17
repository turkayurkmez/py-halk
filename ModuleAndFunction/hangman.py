#Amaç:
# 1. Bir kelime listesi içinden rastgele kelime seç.
import random


def getRandomWord(word_list:list):
    """ Verilen kelime listesi içerisinden rastgele bir kelime seçer """
    return random.choice(word_list)

# 2. Seçilen kelimeyi ----- gibi göster
def displayPuzzle(word:str, guessed_letters:list):
    """ Kelimeyi bulmacaya dönüştürür """
    puzzle = ""
    for letter in word:
        if letter in guessed_letters:
            puzzle += letter + " "
        else:
            puzzle += "_ "

    return puzzle.strip()    
    
# 3. Kullanıcıdan harf iste
def getLetterFromUser():
    """ Kullanıcıdan harf alan fonksiyon """
    while True:
        letter = input("Bir harf tahmin edin").lower()
        if len(letter) == 1 and letter.isalpha():
            return letter
        else:
            print("sadece harf girin")
# 4. Eğer harf varsa karşılık gelen - işaretini harfe çevir a--a
#  .           yoksa hakkını 1 azalt
def hangman():
    """Oyunu başlatan fonksiyon"""
    word_list = ["pyhton","csharp","java","javascript"]
    word = getRandomWord(word_list)
    attempts = 7
    guessed_letters = []

    while attempts > 0:
        print("\nKalan deneme sayısı:",attempts)
        print("Tahmin edilen harfler:",guessed_letters)
        print("Kelime: ", displayPuzzle(word,guessed_letters))

        guess = getLetterFromUser()
        guessed_letters.append(guess)

        if guess not in word:
            attempts-=1
            print("yanlış tahmin")
        
        if all(letter in guessed_letters for letter in word):
            print("Tebrikler! Kelime:",word)
            break
    else:
        print("\n Üzgünüm deneme hakkınız kalmadı! Doğru kelime: ",word)

    if is_renew_game():
        hangman()



# 5. Kelime bulunana dek devam et...
def is_renew_game():
    while True:
        response = input("Tekrar oynamak ister misiniz (e/h)").lower()
        if response in ['e','h']:
            return response == 'e'
        else:
            print("Lütfen e ya da h giriniz!")