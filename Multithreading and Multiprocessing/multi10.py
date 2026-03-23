# Design python application which creates two thread named as even and odd. Even
# thread will display first 10 even numbers and odd thread will display first 10 odd
# numbers.

import os
import threading

def even():
    print("Even Thread")
    count = 0
    for i in range(100):
        if i%2==0 and count < 10:
            print(i)
            count += 1

def odd():
    print("Odd Thread")
    count = 0
    for i in range(100):
        if i%2!=0 and count < 10:
            print(i)
            count += 1


def main():
    print("Inside main")
    thread1 = threading.Thread(target=even)
    thread2 = threading.Thread(target=odd)

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

if __name__ == "__main__":
    main()
