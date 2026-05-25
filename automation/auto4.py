# Design automation script which accept directory name and two file extensions from user.
# Rename all files with first file extension with the second file extension.
# Usage : DirectoryRename.py “Demo” “.txt” “.doc”
# Demo is name of directory and .txt is the extension that we want to search and rename with .doc.
# After execution this script each .txt file gets renamed as .doc.

import os
from sys import *
from pathlib import Path
import shutil

def main():
    print("----------Automation program to display file from specific folder with required extension.---------")
    print("Script Name:", argv[0])
    print("No of arguments accepted:", len(argv)-1)

    if len(argv) >4 or len(argv) <3:
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

    if len(argv) == 4:
        try:
            if argv[1]:
                if os.path.exists(argv[1]):
                    if os.listdir(argv[1]):
                        current_dir =Path(r"D:\Python 2026\Repository code\python\\automation\\" + argv[1])

                        # Loop through all .txt files in the directory
                        for file in current_dir.glob("*"+argv[2]):
                            file.rename(file.with_suffix(argv[3]))

                else:
                    print("Folder not found!")

        except Exception as e:
            print(e)
            print("Exception while executing the script.")
            print("Please check the input or contact the developer.")


if __name__ == "__main__":
    main()
