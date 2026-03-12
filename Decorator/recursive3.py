def factorial(n):
    if n == 0 :                      # base case
        return 1
    else:
        return n * factorial(n-1)    # recursive case

def main():
    fno = int(input("Enter a number: "))
    print("Factorial of number",fno, " :",factorial(fno))

if __name__ == '__main__':
    main()
