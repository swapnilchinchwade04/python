# Write a recursive program which display below pattern.
# Input : 5
# Output : 5 4 3 2 1

def custom_pattern(no):
    temp = 0
    if temp < no:
        temp = no
        no = no - 1
        print(temp, end=" ")
        custom_pattern(no)

def main():
    print("Program to display * pattern.")
    no = int(input("Enter no: "))
    custom_pattern(no)

if __name__ == "__main__":
    main()


