# Design automation script which display information of running processes as its name, PID,
# Username.
# Usage : ProcInfo.py

import os
from sys import *
import multiprocessing
import psutil

def main():
    print("Automation Script to display information of running process.")
    print("Script Name:", argv[0])
    print("No of arguments:", len(argv))

    if len(argv) < 1 :
        print("Invalid number of arguments.")
        print("Use -u for help.")
        print("Use -h for help.")

    if len(argv) == 2:
        if argv[1] == "-u" or argv[1] == "-U":
            print("Usage : ApplicationName")
            exit()
        if argv[1] == "-h" or argv[1] == "-H":
            print("Script ot display information of running process.")
            exit()

    if len(argv) == 1:
        try:
            for proc in psutil.process_iter(['pid', 'name', 'username']):
                print(f"PID: {proc.info['pid']} - Name: {proc.info['name']} - User Name: {proc.info['username']}")

        except Exception:
            print(Exception)


if __name__ == "__main__":
    main()