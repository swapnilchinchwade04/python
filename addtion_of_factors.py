# Write a program which accept one number form user and return addition of its factors.
def main():
    print("Program to get number addition of its factors.")
    print("Please enter number.")
    no1 = int(input())
    ret = 0
    for i in range(1, no1 + 1):
        if no1 % i == 0:
            ret = ret + i

    print("Result: ", ret)


if __name__ == "__main__":
    main()