# Design python application which creates three threads as small, capital, digits. All the
# threads accepts string as parameter. Small thread display number of small characters,
# capital thread display number of capital characters and digits thread display number of
# digits. Display id and name of each thread.

import os
import threading

def small_letter(user_input):
    print("Inside Small Letter")
    print("Thread 1 Name", threading.current_thread().name)
    print("Thread 1 ID", threading.get_ident())
    sum = 0
    for i in range(len(user_input)):
        if user_input[i].islower() :
            sum += 1
    print("Count of small characters in string",sum)
    print()


def capital_letter(user_input):
    print("Inside Capital Letter")
    print("Thread 2 Name", threading.current_thread().name)
    print("Thread 2 ID", threading.get_ident())
    sum = 0
    for i in range(len(user_input)):
        if user_input[i].isupper():
            sum += 1
    print("Count of Capital characters in string", sum)
    print()

def digits_letter(user_input):
    print("Inside Digit Letter")
    print("Thread 3 Name", threading.current_thread().name)
    print("Thread 3 ID", threading.get_ident())
    sum = 0
    for i in range(len(user_input)):
        if user_input[i].isdigit():
            sum += 1
    print("Count of digit characters in string", sum)
    print()


def main():
    print("Inside main")
    print("Enter your input which contains small, capital, digits letters")
    user_input = input()
    #print(user_input)

    thread1 = threading.Thread(target=small_letter, args=(user_input,))
    thread2 = threading.Thread(target=capital_letter, args=(user_input,))
    thread3 = threading.Thread(target=digits_letter, args=(user_input,))

    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()




if __name__ == "__main__":
    main()