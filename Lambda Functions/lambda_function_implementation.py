def main():

    print("Lambada function implementation")
    print("Enter numbers for addition")
    no1= int(input())
    no2= int(input())

    #defining regular function
    def add_numbers(no1,no2):
        return no1+no2

    ret = add_numbers(no1,no2)
    print("Addition of 2 numbers is {} with regular function:".format(ret))

    #defining lambda function
    lf = lambda no1,no2: no1+no2
    ret2  = lf(no1, no2)
    print("Addition of 2 numbers is {} with lambda function:".format(ret2))

if __name__ == "__main__":
    main()

