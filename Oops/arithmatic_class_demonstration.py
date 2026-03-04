#Arithmetic class with two instance variables as Value1 ,Value2
# along with instance methods inside class as Accept(), Addition(), Subtraction(),Multiplication(), Division().
class Circle:
    def __init__(self):
        self.val1 = 0.0
        self.val2 = 0.0

    def accept(self ):
        print ("Please enter 1st number.")
        self.val1 =float(input())

        print("Please enter 2nd number.")
        self.val2 = float(input())

    def Addition(self):
        print("Addition of number is : ",self.val1+self.val2)


    def Subtraction(self):
        print("Subtraction of number is : ",self.val1-self.val2)


    def Multiplication(self):
        print("Multiplication of number is : ",self.val1*self.val2)

    def Division(self):
        print("Division of number is : ",self.val1/self.val2)



def main():
    print("Demonstration of Arithmatic class.")

    obj1 = Circle()
    obj1.accept()
    obj1.Addition()
    obj1.Subtraction()
    obj1.Multiplication()
    obj1.Division()

if __name__ == "__main__":
    main()