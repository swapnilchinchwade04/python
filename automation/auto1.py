# Import statement if necessary.
from sys import *

# Entry point of automation script.
def main():
    print("-----------------------Automation Program 1.-----------------------")
    print("Script Name: ", argv[0])
    print("Number of arguments accepted:", len(argv)-1)

    if (len(argv) > 3) or (len(argv) < 2):
        print("Invalid number of arguments.")
        exit()

    if argv[1] == "-u" or argv[1] == "-U":
        print("Script is used for addition of two numbers")
        exit()

    if argv[1] == "-h" or argv[1] == "-H":
        print("Help: Name_of_script First_Argument Second_Argument")

if __name__ == "__main__":
    main()
