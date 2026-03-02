from functools import reduce


def main():

    print("Program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers. ")
    iplist = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

    # Filter()
    flist = list(filter(lambda x : 70 <= x <= 90, iplist))
    print("Filter output: ",flist)

    #Map()
    mlist = list (map(lambda x : x+10, flist))
    print("Map output: ", mlist)

    #Reduce()
    res = reduce(lambda x, y : x * y, mlist)
    print("Reduce output: ", res)


if __name__ == "__main__":
    main()
