def factirialfun(no, res= 0):
    if no>0:
        if res == 0:
            res = no * (no -1)
        elif no==1:
            res = res
        else:
            res = res * (no - 1)
        factirialfun(no-1, res)
        return res
    print("Output: ", res)


def main():
    print("Program to display factorial of number.")
    no = int(input("Enter the number: "))
    #print("factorial of Number : ",)
    factirialfun(no)


if __name__ == "__main__":
    main()