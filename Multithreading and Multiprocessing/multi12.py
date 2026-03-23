# Design python application which creates two threads as evenlist and oddlist. Both the
# threads accept list of integers as parameter. Evenlist thread add all even elements
# from input list and display the addition. Oddlist thread add all odd elements from input
# list and display the addition.

import os
import threading

def evenlist(numbers):
    print("Inside Evenlist")
    sum = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            print(numbers[i])
            sum += numbers[i]
    print("Sum of even list items :", sum)


def oddlist(numbers):
    print("Inside Oddlist")
    sum = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            print(numbers[i])
            sum += numbers[i]
    print("Sum of odd list items :", sum)


def main():
    print("Inside main")
    userlist = []
    for i in range(5):
        no = int(input("Enter no. : "))
        userlist.append(no)

    thread1 = threading.Thread(target = evenlist , args = (userlist,))
    thread2 = threading.Thread(target = oddlist , args = (userlist,))

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()