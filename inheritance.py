class Account:
    def __init__(self, title=None,balance=0):
        self.title=title
        self.balance=balance
    
    
class SavingsAccount(Account):
    def __init__(self, title, balance,interestRate):
        Account.__init__(self, title=None,balance=0)
        self.interestRate=interestRate

s_1=SavingsAccount("mark", 5000,5)

