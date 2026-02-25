def main():
    print("Implementation of Advance functions")

    # function which accept nothing and return nothing
    def function1():
        print("Hellow world!")

    # function which accept value and return nothing.
    def function2(val2):
        print("Inside function2 :")
        print("Accepted value is :", val2)

    # function which accept value and return value
    def function3(val3):
        print("Inside function3 :")
        print("Accepted value is :", val3)
        return val3

    # function which accept multiple values and return multiple values
    def function4(val5, val6):
        print("Inside function4 :")
        add  = val5 + val6
        sub = val5 - val6
        return add, sub

    # function which calls another function which is outside it.
    def function5():
        print("Inside function5 :")
        function1()

    # function which contains another nested function defined in it.
    def function6():
        print("Inside function6 :")
        def InnerFunction():
            print("Inside inner function6 :")
        InnerFunction()

    no = 22
    function1()
    function2(no)
    ret = function3(no)
    print(" Return value is :",ret)


    ret1, ret2 = function4(10, 12)
    print("Addition is : ", ret1)
    print("Subtraction is : ", ret2)
    function5()

    function6()


if __name__ == "__main__":
    main()