from sys import *

def Addition(num1,num2):
    return num1+num2

def main():
    print("--------------------- Automation Program 2 ---------------------")
    print("Script Name:", argv[0])
    print("No. of arguments accepted", len(argv)-1)

    if(len(argv) > 3) or (len(argv) < 2):
        print("Invalid no. of arguments.")
        print("Use -u flag for usage.")
        print("Use -h for help")

    if len(argv) == 2:
        if argv[1] == "-u" or argv[1] == "-u":
            print("Script is used to perform addition of two numbers.")
            exit()
        elif argv[1] == "-h" or argv[1] == "-h":
            print("Help: Name_of_Script First_Argument Second_Argument")
            exit()
        else:
            print("There is no such flag.")
            exit()

    if len(argv) == 3:
        try:
            iRet= Addition(int(argv[1]), int(argv[2]))
            print("Addition is: ", iRet)
        except Exception:
            print("Exception while executing the script")
            print("Please check the input or contact the developer")

# Starter of automation script.
if __name__ == "__main__":
    main()

