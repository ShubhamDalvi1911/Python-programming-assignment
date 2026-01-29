'''Write a Python program to implement a class named BankAccount with the following requirement:
   - The class should contain two instance variables:
     - Name (Account holder Name)
     - Amount (Account balance)
   - The class should contain one class variable:
     - ROI (Rate of Intrest), initialized to 10.5
   - Define a constructor (__init__) that accepts Name and initial Amount.
   - Implement an instance method:
     - Display() - display account holder name and current balance
     - Deposit() - accepts an amount from the user and adds it to balance
     - withdraw() - accepts an amount from the user and subtracts it from balance(withdrawal is allowd only if sufficient balance exists)
     - CalculateInterest() - calculates and returns interest using formula: Interest = (Amount * ROI) / 100
  - Create multiple objects and demonstrate all methods.'''

class BankAccount:
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print(f"Account Holder Name: {self.Name} and Current Balance: {self.Amount}")

    def Deposit(self):
        Damount = int(input("Enter amount which you want to Deposit: "))
        self.Amount = self.Amount + Damount
        print(f"Your account has been creadited {Damount}. Available balance {self.Amount}.")

    def Withdraw(self):
        Wamount = int(input("Enter amount which you wnat to Withdraw: "))
        if self.Amount - Wamount < 0:
            print("Low Balance!")
        else:
            self.Amount = self.Amount - Wamount
            print(f"Your account has been Debited {Wamount}. Available balance {self.Amount}.")

    def CalculateIntrest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest
    
Obj1 = BankAccount("Shubham Dalvi", 100000)
Obj2 = BankAccount("Bhushan Giramkar", 200000)
Obj3 = BankAccount("Sahil Bansode", 300000)

Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw()
print("Interest On Your account is ",Obj1.CalculateIntrest())