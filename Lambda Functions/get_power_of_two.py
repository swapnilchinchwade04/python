Powerx = lambda a : a*a

def main():
    print("Program which contains one lambda function which accepts one parameter and return power of two. ")
    print("Please enter number to find power of two.")
    no = int(input())
    op = Powerx(no)
    print("Output: ",op)


if __name__ == "__main__":
    main()

