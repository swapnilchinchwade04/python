# Write a program which contains one function named as ChkNum() which accept one
# parameter as number. If number is even then it should display “Even number” otherwise
# display “Odd number” on console.
# Input : 11 Output : Odd Number
# Input : 8 Output : Even Number

def chkNum(no):
    if no%2 == 0:
        print("even number")
    else:
        print("odd number")

def main():
    no1 = int(input("Enter number: "))
    chkNum(no1)

if __name__ == '__main__':
    main()
