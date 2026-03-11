def Division(A, B):  # 0X100
    Ans = 0.0
    Ans = A / B
    return Ans


def SmartDivision(Function_name):  # Function_name -> 0X100  #Decorator
    def Inner(a, b):  # 0X200
        print(a, b)
        if a < b:
            a, b = b, a  # swaping of values of a in b
        return Function_name(a, b)  # return 0X100(_,_)  # calling function within function

    return Inner  # return 0X200


Division = SmartDivision(Division)  # Division = SmartDivision(0X100)


# Global line. 1st this line is going to execute. Its self executable line
# SmartDivision is actually refering to inner function of SmartDivision function


def main():
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))
    ret = Division(no1, no2)  # 0X200(5,10)

    print("Division is:", ret)


if __name__ == "__main__":
    main()