#refering class defined on another/file

from BankAccount import BankAccount
#vere oru filinnu eduthondvarunu values

class SavingsAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)


    def calculate_interest(self):
        interest = self.balance*0.05
        print(f"Intrest of Savings Account :{interest}")
    
    
