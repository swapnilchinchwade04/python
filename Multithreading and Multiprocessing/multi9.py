# threading
import os
import multiprocessing

def square(x):
    print("PID is : ",os.getpid())
    return x * x

def main():
    data = [5,2,7,3,1]
    p = multiprocessing.Pool()
    result = list()
    result = p.map(square, data)
    print("Result: ",result)

if __name__ == "__main__":
    main()
