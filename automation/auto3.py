# Design automation script which accept directory name and file extension from user.
# Display all files with that extension.
# Usage : DirectoryFileSearch.py “Demo” “.txt”
import os
from sys import *

def main():
    print("----------Automation program to display file from specific folder with required extension.---------")
    print("Script Name:", argv[0])
    print("No of arguments accepted:", len(argv)-1)

    if len(argv) > 3  or len(argv) < 2:
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

    if len(argv) == 3:
        try:
            print("Inside try")
            if argv[1]:
                if os.path.exists(argv[1]):
                    print("Folder Exists!")
                    if  os.listdir(argv[1]):
                        files = os.listdir(argv[1])
                        for file in files:
                            extension = file.split(".")[-1]
                            if extension == "txt":
                                print("File Name:", file)

                    else:
                        print("Folder empty!")
                else:
                    print("Folder Not Exists!")

        except Exception:
            print("Exception while executing the script.")
            print("Please check the input or contact the developer.")



if __name__ == "__main__":
    main()