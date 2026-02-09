#Write a program which accept number from user and print that number of “*” on screen.
#Input : 5 Output : * * * * *

def main():
    no1 = int(input("Enter number to display * : "))
    strop  =''
    while no1 > 0 :
        strop = strop + "* "
        no1 -= 1
    print(strop)

if __name__ == '__main__':
    main()