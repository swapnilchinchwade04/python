# Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
# for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
# parameters as number and perform the operation. Write on python program which call all the
# functions from Arithmetic module by accepting the parameters from user.

import arithmetic_module as arth

def main():
    print("Please enter 1st number :")
    no1 = int(input())
    print("Please enter 2nd number :")
    no2 = int(input())
    print("Addition of 2 number :", arth.Add(no1,no2))
    print("Subtraction of 2 number :", arth.Sub(no1,no2))
    print("Multiplication of 2 number :", arth.Mul(no1,no2))
    print("Division of 2 number :", arth.Division(no1,no2))

if __name__ == '__main__':
    main()

