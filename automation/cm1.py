from sys import *

def add1(arg1,arg2):
    print(int(arg1)+int(arg2))

def main():
    print("No of command lines are:", len(argv))
    print("Name of application: ", argv[0])
    print("First argument:", argv[1])
    print("Second argument:",argv[2])
    add1(argv[1], argv[2])

if __name__ == "__main__":
    main()
