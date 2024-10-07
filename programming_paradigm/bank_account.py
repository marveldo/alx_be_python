
class BankAccount:

    def __init__(self, account_balance : int = 0):
        self.account_balance = account_balance
    
    def deposit(self , amount : int):
        self.account_balance += amount
    def withdraw(self, amount : int):
        if self.account_balance - amount > 0 :
            self.account_balance -=  amount
            return True
        else :
            return False
    def display_balance(self):
        print(f'Current Balance: ${self.account_balance}')
    
        
