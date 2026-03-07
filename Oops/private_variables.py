class Demo:
    def __init__(self):
        self.A = 10
        self.__B = 20    # private variable of class abstraction

    def fun(self):
        print("Inside Fun: ")
        print(self.A)
        print(self.__B)    #private instance variable

    def __gun(self):  # private method
        print("Inside gun.")


def main():
    obj = Demo()
    print(obj.A)
    #print(obj.B)  # private variable, we can't use inside main
    obj.fun()
    #obj.gun()  # can't access private method

if __name__ == "__main__":
    main()

