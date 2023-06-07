class Bank:
     def __init__(self, account_number, account_balance, account_holder) :
          self.account_number = account_number
          self. account_balance = account_balance
          self.account_holder = account_holder
     def deposit(self, depo):
          self.account_balance += depo
     def withdrawal(self, withd):
          if withd >= self.account_balance:
               print (f"Your Bank Balance is Insuffient, your bank balance is {self.balance}") 
          elif  withd <= self.account_balance:
             self.account_balance -= withd
             print(f" Withdrawal Successful!, ") 
     def  bank_balance (self):
         print ("Your account balance is  {self.account_balance}")


account = Bank("123456", 100000, "Ben Kipkulei Kaimogul")
account.deposit(200)
account.withdrawal(300)

print(account.account_balance)