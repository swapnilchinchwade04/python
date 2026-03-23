# Design python application which contains two threads named as thread1 and thread2.
# Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
# screen. After execution of thread1 gets completed then schedule thread2.

import os
import threading

def custom1():
    for i in range(1, 51):
        print('Thread 1: ', i)

def custom_2():
    for i in range(50, 0, -1):
        print('Thread 2: ', i)
    print()

def main():
    print("Inside main")
    thread1 = threading.Thread(target=custom1)
    thread2 = threading.Thread(target=custom_2)

    thread1.start()
    while thread1.is_alive():
        pass
    thread2.start()


if __name__ == "__main__":
    main()