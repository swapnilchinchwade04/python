# Design automation script which accept directory name and display checksum of all files.
# Usage : DirectoryChecksum.py “Demo”
# Demo is name of directory.

import os
from pathlib import Path
from sys import *
import hashlib

def main():
    print("---------------------- Automation script which accept directory name and display checksum of all files ----------------------")
    print("Script Name:", argv[0])
    print("No of arguments accepted : ", len(argv)-1 )

    if len(argv) >2 or len(argv) <1:
        print("Invalid number of arguments!")
        print("Use -u for usage.")
        print("Use -h for help")
        exit()

    if len(argv) == 2:
        if argv[1] == "-u" or argv[1]== "-U":
            print("Script is used for finding all files with specified extension in required directory.")
            exit()
        if argv[1]=="-h" or argv[1] == "-H":
            print("Help: Name_of_Script Directory_Name File_Extension")
            exit()

    if len(argv) == 2:
        try:
            if argv[1]:
                if os.path.exists(argv[1]):
                    files = os.listdir(argv[1])
                    print("files: ", files)
                    dir_path = os.path.dirname(os.path.abspath(__file__))
                    for file in files:
                        with open(dir_path+ '\\' + argv[1] +'\\'+file, "rb") as f:
                            print("File Name: ", file)
                            digest = hashlib.file_digest(f, "sha256")
                            print("Checksum of file: ",digest.hexdigest())
                            print("\n")
                else:
                    print("Directory does not exist!")

        except Exception:
            print(Exception)
            print("Invalid number of arguments!")
            print("Use -u for usage.")

if __name__ == "__main__":
    main()
