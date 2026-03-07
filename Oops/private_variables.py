class Demo:
    def __init__(self):
        self.A = 10
        self.__B = 20    # private variable of class abstraction

    def fun(self):
        print("Inside Fun: ")
        print(self.A)
        print(self.__B)    #private instance variable

def main():
    obj = Demo()
    print(obj.A)
    #print(obj.B)  # private variable, we can't use inside main
    obj.fun()

if __name__ == "__main__":
    main()

