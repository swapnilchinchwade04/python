# Write a program which accept one number and display below pattern.
# Input : 5
# Output :
#  * * * * *
#  * * * *
#  * * *
#  * *
#  *

def main():
    no1 = int(input("Enter no1: "))
    for i in range(1, no1+1):
        for j in range(1, no1+1):
            print('*', end=" ")
        print("\n")
        no1 -= 1

if __name__ == '__main__':
    main()
