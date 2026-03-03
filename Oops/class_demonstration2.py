class Demo:
    def __init__(self, val1, val2):
        self.i= val1
        self.j = val2
    def add(self):
        return self.i + self.j

def main():
    print("Enter 1st number")
    no1= int(input())
    print("Enter 2nd number")
    no2= int(input())
    obj1 = Demo(no1, no2)
    res = obj1.add()
    print("Addition of numbers is:", res)


if __name__ == "__main__":
    main()