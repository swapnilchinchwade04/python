class Base1:
    def __init__(self):
        print("Inside Base1 Class")
        self.A = 10
    def fun(self):
        print("Fun Method of Base1 Class")

class Base2:
    def __init__(self):
        print("Inside Base2 Class")
        self.B = 20
    def gun(self):
        print("Gun Method of Base2 Class")

class Derived(Base1, Base2):
    def __init__(self):
        self.C = 30
        Base1.__init__(self)
        Base2.__init__(self)
        print("Inside Derived Class")

    def sun(self):
        print("Sun Method of Derived Class")

def main():
    obj1 = Derived()
    print(obj1.A)
    print(obj1.B)
    print(obj1.C)
    print()
    obj1.fun()
    obj1.gun()
    obj1.sun()

if __name__ == "__main__":
    main()
