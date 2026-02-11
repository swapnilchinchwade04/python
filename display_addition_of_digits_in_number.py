# Write a program which accept number from user and return addition of digits in that number.
# Input : 5187934
# Output : 37

def main():
    print("Please enter the number.")
    no1 = int(input())
    sum1 = 0
    m = 0
    while no1 > 0:
        m = no1 % 10
        sum1 = sum1 + m
        no1 = int(no1 / 10)
    print("Addition of digits in number is: ", sum1)


if __name__ == "__main__":
    main()



