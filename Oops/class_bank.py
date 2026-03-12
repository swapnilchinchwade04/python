# Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount.
# That class contains one class variable as ROI which is initialise to 10.5.
# Inside init method initialise all name and amount variables by accepting the values from user.
# There are Four instance methods inside class as Display(), Deposit(), Withdraw(),
# CalculateIntrest().
# Deposit() method will accept the amount from user and add that value in class instance variable
# Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount
# from class instance variable Amount.
# CalculateIntrest() method calculate the interest based on Amount by considering rate of interest
# which is Class variable as ROI.
# And Display() method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects.
from Oops.class_book_store import BookStore


class BankAccount:
    roi =10.5
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


    def Display(self):
        print("Name:",self.name)
        print("Amount:",self.amount)

    def Deposit(self,temp):
        #self.name = input("Enter User Name: ")
        #self.amount = int(input("Enter Amount: "))
        self.amount =  self.amount + temp
        print("Amount after deposit : ",self.amount)

    def Withdraw(self, temp):
        self.amount =  self.amount - temp
        print("Balance after withdrawal:", self.amount)

    def CalculateIntrest(self):
        interest = self.amount * (BankAccount.roi / 100)
        print("Interest on amount", interest)


def main():
    obj1 = BankAccount("John",1200)
    obj1.Display()
    obj1.Deposit(100)
    obj1.Withdraw(50)
    obj1.CalculateIntrest()


if __name__ == "__main__":
    main()
