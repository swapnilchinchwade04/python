def main():
    print(
        "Program to accept N numbers from user and store it into List. Return addition of all elements from that List.")
    print("Number of elements:")
    no1 = int(input())
    data = []
    sum1 = 0
    temp =0
    if no1 > 0:
        for i in range(no1):
            temp = int(input())
            data.append(temp)
            sum1 = sum1+temp
        print(data)
        print("Sum of all elements:", sum1)



if __name__ == "__main__":
    main()