import os
import threading


def fun(x):
    print("PID : ", os.getpid())
    print("PPID : ", os.getppid())
    print("Inside Fun.")
    for i in range(x):
        print("Fun : ", i)

def gun(x):
    print("PID : ", os.getpid())
    print("PPID : ", os.getppid())
    print("Inside Gun")
    for i in range(x):
        print("Gun : ", i)

def main():
    no = 5
    thread1 = threading.Thread(target = fun, args=(no,))
    thread2 = threading.Thread(target = gun, args =(no,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print("END of main")

if __name__ == "__main__":
    main()
