#Write a program which accept name from user and display length of its name.
#Input : Everest Output : 7

def main():
    print("Program to accept name from user and display length of its name.")
    print("Please enter name :")
    user_input = input()
    print("Length of name is : ", len(user_input))

if __name__ == '__main__':
    main()