from functools import reduce


def main():
    print("Filter Map & Reduce function implementation")
    arr = [8,9,5,16,2,4,21,30,11]
    print("Input:", arr)
    print("Filter Function to display even numbers from input:")
    evearr= list(filter(lambda x : x%2 == 0, arr))
    print("Filter() Output:", evearr)


    print("Map Function to add 2 in list elements:")
    print("Input:", evearr)
    modarry = list(map(lambda no : no+2, evearr))
    print("Map() Output:", modarry)

    print("Reduce Function to show addition of list elements:")
    sumarr = reduce(lambda x,y : x+ y , modarry)
    print("Reduce() Output:", sumarr)



if __name__ == "__main__":
    main()
