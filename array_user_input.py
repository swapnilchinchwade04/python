import array as ARR
def main():
    data = ARR.array('i')
    no1 = int(input("Enter no of element you want to enter in array: "))
    for i in range(no1):
        data.append(int(input()))

    print("Length of array is :", len(data))
    print("Type of array is :",type(data))

    for no in range(len(data)):
        print(data[no], end="\t")

if __name__ == "__main__":
    main()