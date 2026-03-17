# Threading
import os
import threading


def fun(x):
    print("\nInside Fun.")
    print("\nPID : ", os.getpid())
    print("\nPPID : ", os.getppid())
    print("\nThread name of Fun :", threading.current_thread().name)

    for i in range(x):
        print("Fun : ", i)

def gun(x):
    print("\nInside Gun")
    print("\nPID : ", os.getpid())
    print("\nPPID : ", os.getppid())
    print("\nThread name of Gun :", threading.current_thread().name)

    for i in range(x):
        print("Gun : ", i)

def main():
    no = 5
    print("\nMain PID : ", os.getpid())
    print("\nThread name of Main :", threading.current_thread().name)

    thread1 = threading.Thread(target = fun, args=(no,))
    thread2 = threading.Thread(target = gun, args =(no,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print("END of main")

if __name__ == "__main__":
    main()
