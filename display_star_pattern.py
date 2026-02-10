# Write a program which accept one number and display below pattern.
# Input : 5
# Output :
#  * * * * *
#  * * * * *
#  * * * * *
#  * * * * *
#  * * * * *


def main():
    print("Please enter number :")
    k = int(input())
    j,i = k,k
    l =''
    while (i>0):
        while(j>0):
            l = l + '* '
            j -= 1
        print(l)
        i -= 1

if __name__ == '__main__':
    main()
