import array as ARR
def main():
     arr1 = ARR.array('i',[10, 20, 30, 40])
     print(arr1)
     print("Length of list is: ", len(arr1))
     print("Type of array is: ", type(arr1))

     print("Data from array:")
     for i in range(len(arr1)):
         print(arr1[i], end=" ")


if __name__ == "__main__":
    main()
