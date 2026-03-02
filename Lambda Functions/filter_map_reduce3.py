from functools import reduce

from primePy import primes
def main():
    print("Program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers.")

    print("Enter numbers for list:")
    ulist = []
    for i in range(4):
        ulist.append(int(input()))
    print("User input: ", ulist)

    #filter
    print("Filter :")
    flist = list(filter(lambda x : primes.check(x), ulist))
    print("Filter output: ", flist)

    #map
    print("Map : ")
    mlist = list(map(lambda x: x*2, flist))
    print("Map output: ", mlist)

    #reduce
    print("Reduce : ")
    res = reduce(lambda x,y  : x if x>y else y, mlist)
    print("Reduce output: ", res)


if __name__ == '__main__':
    main()