


from BankAccount import BankAccount,abstractmethod
#INHERITANCE : WE INHERIT METHODS AND PROPERTIES OF PARENT CLASS

class CurrentAccount(BankAccount):
    def  __init__(self,balance):
        super().__init__(balance)
    

    def dummy_method(self):
        print("dummy method")
    
    def calculate_interest(self):
        interest_current = self.balance * 0
        print(f"The interest of Current Account :{interest_current}")
