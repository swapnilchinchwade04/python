# Design automation script which accept directory name from user and create log file in that
# directory which contains information of running processes as its name, PID, Username.
# Usage : ProcInfoLog.py Demo
# Demo is name of Directory.

import os
from sys import argv
import psutil


def processinfolog(path):
    flag  = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
        exits = os.path.isdir(path)
        if exits :
            print("Path : " + path)
            with open(path+'\ProcessLog.txt', 'a') as log_file:
                log_file.write(f"PID   Name                 User Name " + "\n")
                for proc in psutil.process_iter(['pid', 'name', 'username']):
                    print(f"PID: {proc.info['pid']} - Name: {proc.info['name']} - User Name: {proc.info['username']}")
                    #data = f"PID: {proc.info['pid']} - Name: {proc.info['name']} - User Name: {proc.info['username']}"
                    data = f"{proc.info['pid']} - {proc.info['name']} - {proc.info['username']}"

                    log_file.write(data + "\n")



def main():
    print("Automation Script which accept directory name & stores information of running process in log file.")
    print("Script Name:", argv[0])
    print("No of arguments:", len(argv)-1)

    if len(argv) < 1 or len(argv) > 2:
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

    if len(argv) == 2:
        try:
            processinfolog(argv[1])

        except Exception:
            print("Exception")
            print("Invalid number of arguments.")
            print("Use -u for help.")


if __name__ == "__main__":
    main()