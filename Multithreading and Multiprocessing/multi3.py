import os

def fun(x):
    print("PID : ", os.getpid())
    print("Inside Fun")
    for i in range (x):
        print("Fun : ", i)

def gun(x):
    print("PID : ", os.getpid())
    print("Inside Gun")
    for i in range(x):
        print("Gun : ", i)

def main():
    print("PID : ", os.getpid())
    fun(5)
    gun(10)

if __name__ == "__main__":
    main()
    