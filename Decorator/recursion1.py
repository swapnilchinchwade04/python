import sys
def funR(no):
    print(sys.getrecursionlimit())

    no = no + 1
    funR(no) # Recursive call

def main():
    funR(0)

if __name__ == "__main__":
    main()