print("Demonstration of class.")
class Demo:

    def __init__(self, val1, val2):
        print("Inside init method")
        self.i = val1
        self.j =  val2

    def fun(self):
        print("Inside fun method")
        print(self.i, self.j)

    def add(self):
        print("Inside add method")
        print(self.i + self.j)


# Create object of Demo class
obj1 = Demo(10,20)
# Call to fun method
obj1.fun()
# Create object of Demo class
obj2 = Demo(40,60)
obj2.fun()

# Call to add method to perform addition operation
obj1.add()
obj2.add()
