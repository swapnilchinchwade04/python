# Design python application which creates two threads as evenfactor and oddfactor.
# Both the thread accept one parameter as integer. Evenfactor thread will display
# addition of even factors of given number and oddfactor will display addition of odd
# factors of given number. After execution of both the thread gets completed main
# thread should display message as “exit from main”.

import os
import threading


def Evenfactor(no):
    print("Inside Evenfactor")
    sum = 0
    for i in range(1, no+1):
        if no%i ==0 :
            if i % 2 == 0:
                sum += i
    print("Sum of even factors :", sum)

def oddfactor(no):
    print("oddfactor")
    sum =0
    for i in range(1, no+1):
        if no % i == 0:
            if i % 2 != 0:
                sum +=i
    print("Sum of odd factors :", sum)



def main():
    print("Inside main")
    no = int(input("Enter no: "))

    thread1 = threading.Thread(target = Evenfactor, args = (no,))
    thread2 = threading.Thread(target = oddfactor, args = (no,))

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()