from CurrentAccount import CurrentAccount
# from SimpleAccount import SimpleAccount
from SavingsAccount import SavingsAccount


#creating n object of class "simpleaccount"
# sAccount1 =SimpleAccount()
# sAccount1.method1()

#creating an object for BankAccount()
# not possible because  we cannot create an object of an abstract class
# bankAcc1 = BankAccount() # it s an abstract class so we cant create an object for that
# bankAcc1.deposit

ca1 = CurrentAccount(8000)
ca1.dummy_method()
ca1.deposit(2000)
# # print(f"tha balance amount is : {ca1.__balance}")#this cannot be done bcz it is protected in parent class

# # to display the balance use the function from the parent class
# ca1.display_balance()
# ca1.withdraw(4000)

# ca1.display_balance()
ca1.withdraw(5000)
# ca1.display_balance()
ca1.calculate_interest()

sa1=SavingsAccount(3000)
# sa1.display_balance()
sa1.withdraw(1000)
# sa1.display_balance()
sa1.deposit(1000)
# sa1.display_balance()
sa1.calculate_interest()

# C:\Users\DELL\Desktop\AIML\PYTHON\OOPs\BankAccountManagementSystem\BankAccount.py