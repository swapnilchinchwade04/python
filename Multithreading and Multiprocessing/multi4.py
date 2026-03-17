from multiprocessing import Process
import os


def fun(x):
    print("PID :", os.getpid())
    print("PPID :", os.getppid())
    print("Inside Fun.")
    for i in range(x):
        print("Fun : ", i)

def gun(x):
    print("PID :", os.getpid())
    print("PPID :", os.getppid())
    print("Inside Gun.")
    for i in range(x):
        print("Gun : ", i)

def main():
    No=5
    print("PID :", os.getpid())
    process1 = Process(target=fun, args=(No,))
    process2 = Process(target=gun, args=(No,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("END of main")

if __name__ == "__main__":
    main()
