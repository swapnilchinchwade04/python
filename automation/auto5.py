# Design automation script which accept two directory names. Copy all files from first directory
# into second directory. Second directory should be created at run time.
# Usage : DirectoryCopy.py “Demo” “Temp”
# Demo is name of directory which is existing and contains files in it. We have to create new
# Directory as Temp and copy all files from Demo to Temp.

import os
from sys import *
import shutil
def main():
    print("----------Automation program to move files from one folder to new folder.---------")
    print("Script Name:", argv[0])
    print("No of arguments accepted:", len(argv) - 1)

    if len(argv) > 3 or len(argv) < 2:
        print("Invalid number of arguments!")
        print("Use -u for usage.")
        print("Use -h for help")
        exit()

    if len(argv) == 2:
        if argv[1] == "-u" or argv[1] == "-U":
            print("Script is used for finding all files with specified extension in required directory.")
            exit()
        if argv[1] == "-h" or argv[1] == "-H":
            print("Help: Name_of_Script Directory_Name File_Extension")
            exit()

    if len(argv) == 3:
        try:
            if argv[1] :
                if os.path.exists(argv[1]):
                    if argv[2]:
                        os.makedirs(argv[2], exist_ok=True)
                        #print(os.path.basename())

                        if os.listdir(argv[1]):
                            files = os.listdir(argv[1])
                            for file in files:
                                print("File inside folder: ",file)
                                dir_path = os.path.dirname(os.path.abspath(__file__))
                                #print("Dir path: ",dir_path)
                                new_dir_path =r"D:\Python 2026\Repository code\python\\automation\\"+argv[2]
                                dest = shutil.move(dir_path+ '\\' + argv[1] +'\\'+file, new_dir_path + '\\' + file)
                                print("Moved file: ", dest)
                else:
                    print("Folder does not exist!")

        except Exception:
            print(Exception)
            print("Exception while executing the script.")
            print("Please check the input or contact the developer.")
if __name__ == "__main__":
    main()