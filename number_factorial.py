# Write a program which accept one number from user and return its factorial.
# Input : 5 Output : 120
from math import factorial


def main():
    print("Please enter number :")
    no1 = int(input())
    ans = 1
    while ( no1 > 0):
        ans *= no1
        no1 -= 1
    print("Factorial of number :",ans)

if __name__ == '__main__':
    main()