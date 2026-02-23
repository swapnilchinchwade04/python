def main():
    print(
        "Program to accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.")
    print(" Number of elements :")
    no1 = int(input())
    data = []
    temp = 0
    print("Enter the numbers :")
    if no1 > 0:
        for i in range(no1):
            temp = int(input())
            data.append(temp)
        print("List element : ", data)
    print("Enter the number to search:")
    no2 =  int(input())
    if data.count(no2) > 0:
        print("Frequency of number : ", data.count(no2))
    else:
        print("Input not available in list."
              )


if __name__ == "__main__":
    main()
