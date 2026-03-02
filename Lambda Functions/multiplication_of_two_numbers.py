MulX = lambda a,b : a*b

def main():
    print("Program which contains one lambda function which accepts two parameters and return its multiplication.")
    print("Enter 1st number")
    no1 = int(input())
    print("Enter 2nd number")
    no2 = int(input())
    print("Multiplication of numbers")
    no3 = MulX(no1,no2)
    print(no3)

if __name__ == "__main__":
    main()
