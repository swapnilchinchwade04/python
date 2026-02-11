# Write a program which accept one number and display below pattern.
# Input : 5
# Output :
#  1
#  1 2
#  1 2 3
#  1 2 3 4
#  1 2 3 4 5

def main():
    print("PLease enter a number")
    no1=int(input())
    for i in range(1,no1+1):
        for j in range(1,i+1):
            print(j,end=" ")
            j += 1
        print('\n')
        i += 1



if __name__ == '__main__':
    main()