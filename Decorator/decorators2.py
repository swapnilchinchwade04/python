def Division(A,B):
    print("Inside Division")
    Ans = 0.0
    Ans = A/B
    return Ans

def SmartDivision(Function_name):
    print("Inside Smart Division")
    def Inner(A,B):
        print("Inside Inner Function")
        if A<B :
            A,B = B,A  # swapping of values
            return Function_name(A,B)
    return Inner

Division = SmartDivision(Division) # Global line 1st this line is going to execute.

def main():
    print("Inside Main Function")
    Ans = Division(2,3)
    print(Ans)

if __name__ == "__main__":
    main()