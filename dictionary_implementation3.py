def main():
    data = {'A':10,'B':20,'C':30,'D':40}
    print("Data is: ", data)
    print("Type of data is :", type(data))
    print("Length of data is :", len(data))
    #print(data[0])  we can't access dictionary with index.
    for keys in data:
        print(keys, data[keys])

if __name__ == "__main__":
    main()