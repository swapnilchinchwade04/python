# Write a recursive program which accept number from user and return
# summation of its digits.
# Input : 879
# Output : 24

def custom_summation(no, sum =0):
    if no > 0:
        sum = int(sum) + int(no%10)
        no = int(no/10)
        custom_summation(no, sum)
        return sum
    print("Output :", sum)

def main():
    print("Program to display custom summation.")
    print("Enter no.")
    no = int(input())
    custom_summation(no)

if __name__ == "__main__":
    main()

