# threading
import os
import multiprocessing

def square(x):
    return x*x

def main():
    data = [5,3,4,6,2,1]
    result = list()
    for i in range(len(data)):
        result.append(square(data[i]))

    print("Result: ",result)

if __name__ == "__main__":
    main()
    