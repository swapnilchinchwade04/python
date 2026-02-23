def main():
    print("Program to accept N numbers from user and store it into List. Return Maximum number from that List.")
    print("Number of elements: ")
    no1 = int(input())
    data = []
    temp = 0
    if no1 > 0:
        for i in range (no1):
            temp = int(input())
            data.append(temp)
        print("List element: ", data)
        print("Maximum number: ", max(data))





if __name__ == "__main__":
    main()