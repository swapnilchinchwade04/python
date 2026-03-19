# Write a recursive program which display below pattern.
# Input : 5
# Output : * * * * *

def pattern_custom(no):
    if no>0 :
        print("*", end =" ")
        no = no -1
        pattern_custom(no)

def main():
    print("Program to display * pattern.")
    print("Enter the no.")
    no1= int(input())
    pattern_custom(no1)

if __name__ == '__main__':
    main()
