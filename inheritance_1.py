class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        self.amount=amount
        self.balance-=self.amount

    def deposit(self, amount):
        self.amount=amount
        self.balance+=self.amount

    def getBalance(self):
        print("Available Balance is:", self.balance) 


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        print("Interest amount is:",(self.interestRate*self.balance)/100)



demo1 = SavingsAccount("Mark", 2000, 5)
demo1.getBalance()
demo1.interestAmount()
demo1.withdrawal(1000)
demo1.getBalance()
demo1.deposit(5000)
demo1.getBalance()