# Design automation script which accept two directory names and one file extension. Copy all
# files with the specified extension from first directory into second directory. Second directory
# should be created at run time.
# Usage : DirectoryCopyExt.py “Demo” “Temp” “.exe”
# Demo is name of directory which is existing and contains files in it. We have to create new
# Directory as Temp and copy all files with extension .exe from Demo to Temp.

import os
from sys import *
import shutil



def main():
    print("-------------------- Automation Program --------------------")
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
            print("Inside Try")
            if argv[1]:
                if os.path.exists(argv[1]):
                    if argv[2]:
                        os.makedirs(argv[2], exist_ok=True)
                        if os.listdir(argv[1]):
                            files = os.listdir(argv[1])

                            print(files)
                            dir_path = os.path.dirname(os.path.abspath(__file__))

                            for file in files:
                                print("File Name:", file)
                                if file.endswith(".exe"):
                                    dest = shutil.move(dir_path + '\\' + argv[1] + '\\' + file, dir_path + '\\' + argv[2] + '\\' + file)
                                    print("Moved file: ", dest)

                else:
                    print("Folder does not exist")
        except Exception:
            print(Exception)
            print("Exception while executing the script.")
            print("Please check the input or contact the developer.")

if __name__ == "__main__":
    main()

