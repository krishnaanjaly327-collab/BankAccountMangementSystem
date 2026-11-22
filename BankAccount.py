from abc import ABC , abstractmethod 


class BankAccount(ABC):
    
    
    def  __init__(self,balance):
        self.__balance = balance

    
    
    def display_balance(self):
        # we are displaying a private information
        print(f"The account balance is {self.__balance}")
        
    
    @property
    def balance(self):
        return self.__balance

    
    
    @balance.setter

    def balance(self,amount):
        if amount<0:
            raise ValueError( "Updated balance  cannot be  a negative value")
        self.__balance = amount
        print(f' Salary  :{self.__balance} ')
    
    def deposit(self,amount):
        if amount>0:
            
            self.__balance =self.__balance+amount
            print(f'Deposit is successful  :{self.__balance} ')
        else:
            print("The deposit amount  must be a positive value")

    
    def withdraw(self,amount):
            
        if (amount>0) and (self.__balance >= amount):
            
            self.__balance =self.__balance - amount
            print(f'Withdrawal is successful  :{self.__balance} ')
       
        elif(self.__balance < amount):
            print(" Insufficient balance")
        else:
            print("The withdrawal amount  must be a positive value")
             
    
    
    # this method   must inherited by the child class        
    @abstractmethod
    def calculate_interest(self):
        pass

    

