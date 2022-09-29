from re import I


class BankAccount:
    

    def __init__(self, int_rate, balance = 0): 
        self.balance = balance
        self.int_rate = int_rate
    
    def deposit(self, amount):
        self.balance += self.balance + amount
        return self
    def withdraw(self, amount):
        self.balance += self.balance - amount
        if self.balance < amount:
            print('Insufficient funds: charging a $5 fee')
            self.balance = self.balance - 5
            return self

    def display_account_info(self):
        print(f'Balance: ${self.balance}')
        return self
    
    def yield_interest(self):
        self.balance = self.balance * self.int_rate
        return self

this_account = BankAccount(1.5,200)

this_account.deposit(200).display_account_info().withdraw(50).yield_interest(1.5)





class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.deposit(200)
    	
    def make_withdraw(self):
        self.withdraw(300)

