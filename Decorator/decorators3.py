def Sub(A,B):
    Ans = 0.0
    Ans = A-B
    return Ans

def SmartSub(Function_name):
    def Inner(A,B):
        if A<B :
            A,B = B, A
        return Function_name(A,B) # calling function within function
    return Inner

Sub = SmartSub(Sub)
#smartSub is actually referring to Inner function of SmartSub

def main():
    no1= int(input("Enter no1: "))
    no2= int(input("Enter no2: "))
    ANS = Sub(no1,no2)
    print("Result :", ANS)

if __name__ == '__main__':
    main()

