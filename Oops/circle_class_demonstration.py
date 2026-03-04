#Circle class with three instance variables as Radius ,Area, Circumference.
class Circle:
    pi= 3.14
    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def accept(self ):
        print ("Please enter radius of circle.")
        self.radius =float(input())

    def calculatearea(self):
        self.area = Circle.pi * self.radius * self.radius


    def calculatecircumference(self):
        self.circumference = 2*Circle.pi*self.radius


    def display(self):
        print("Radius:", self.radius)
        print("Area:", self.area)
        print("Circumference:", self.circumference)




def main():
    print("Demonstration of Circle class.")

    obj1 = Circle()
    obj1.accept()
    obj1.calculatearea()
    obj1.calculatecircumference()
    obj1.display()


if __name__ == "__main__":
    main()