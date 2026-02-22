import array as ARR


def main():
    #to accept float value we are using 'f'
    arr1 = ARR.array('f', [10.2, 20.4, 30.2, 40.9])
    print(arr1)
    print("Length of list is: ", len(arr1))
    print("Type of array is: ", type(arr1))

    print("Data from array:")
    for i in range(len(arr1)):
        print(arr1[i], end=" ")


if __name__ == "__main__":
    main()
