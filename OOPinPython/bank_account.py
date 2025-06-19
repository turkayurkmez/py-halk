import datetime


class BankAcount:
    # Class Variables: Tüm nesneler için ortak:
    bank_name = "X Bank"
    code= "0001"
    count_of_accounts = 0
    rate = 47 
    daily_transfer_limit= 1000000

    account_types = {
        "vadesiz":{"minimum_bakiye":100, "islem_ucreti":2},
        "vadeli":{"minimum_bakiye":1000, "islem_ucreti":0},
        "yatırım":{"minimum_bakiye":10000, "islem_ucreti":5}
    }

    def __init__(self, account_owner, account_tpe="vadesiz", starting_balance=0):
        # instance variables: üretilen nesneye ait:
        self.account_owner = account_owner
        self.account_type = account_tpe
        self.balance = starting_balance
        self.is_active = True
        self.history = []
        self.created_date = datetime.datetime.now()

        #Class variable'a müdahale et:
        BankAcount.count_of_accounts += 1
        self.IBAN = f"TR{BankAcount.code}{1000000 + BankAcount.count_of_accounts}"

        print(f"Toplam hesap sayısı: {BankAcount.count_of_accounts}")

    @classmethod
    def update_rate(cls, new_rate):
        old_rate = cls.rate
        cls.rate = new_rate

        print(f"Faiz oranı güncdellendi %{old_rate} -> %{new_rate}")
        print(f"Bu değişiklik {cls.count_of_accounts} adet hesabı etkiliyor.")

    def calculate_interest(self):
        print("Belirlenen faiz oranı:", self.rate)

    @staticmethod
    def compare_balance(balance1, balance2):
        diff = abs(balance1 - balance2)
        diff_rate = (diff / max(balance1,balance2))*100

        if balance1> balance2:
            print(f"{balance1}, {balance2}'den %{diff_rate:.1f} daha fazla. Fark: {diff: .0f} TL")
        elif balance1 < balance2:
            print(f"{balance1}, {balance2}'den %{diff_rate:.1f} daha az. Fark: {diff: .0f} TL")
        else:
            print("iki bakiye de eşit")

     
