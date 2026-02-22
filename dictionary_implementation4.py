def main():
    data = {"Even": [2, 4, 6, 8], "Odd": [1, 3, 5, 7], "Other": [13.25, 11.5, 17.5]}
    print("Data is: ", data)
    print("Type of data is :", type(data))
    print("Length of data is :", len(data))
    #print(data[0])  we can't access dictionary with index.
    for keys in data:
        print(keys, data[keys])

    print("Data by new for loop:")

    for keys in data:
        print(keys, end=" ")
        for i in range(len(data)):
            print(data[keys][i], end=" ")
        print(" ")
if __name__ == "__main__":
    main()