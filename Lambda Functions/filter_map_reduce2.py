from functools import reduce

evenX = lambda x : x%2 == 0
squareX = lambda x : x*x

def main():
    print("Program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers. ")

    print("Enter number for list:")
    ulist = []
    for i in range(4):
        ulist.append(int(input()))

    print("Input: ", ulist)

    #filter
    flist = list(filter(evenX, ulist))
    print("Filter output : ", flist)

    # map
    mlist = list(map(squareX, flist))
    print("Filter output : ", mlist)


    #reduce
    res = reduce(lambda x,y : x+y, mlist)
    print("Reduce output : ", res)




if __name__ == '__main__':
    main()
