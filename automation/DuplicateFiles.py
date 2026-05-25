# Design automation script which accept directory name and write names of duplicate files from
# that directory into log file named as Log.txt. Log.txt file should be created into current
# directory.
# Usage : DuplicateFiles.py “Demo”

import os
from sys import *
import hashlib

def main():
    print(
        "---------------------- Automation script which find duplicate files from directory ----------------------")
    print("Script Name:", argv[0])
    print("No of arguments accepted : ", len(argv) - 1)

    if len(argv) > 2 or len(argv) < 1:
        print("Invalid number of arguments!")
        print("Use -u for usage.")
        print("Use -h for help")
        exit()

    if len(argv) == 2:
        if argv[1] == "-u" or argv[1] == "-U":
            print("Script is used to find duplicate files from directory.")
            exit()
        if argv[1] == "-h" or argv[1] == "-H":
            print("Help: Name_of_Script Directory_Name File_Extension")
            exit()

    if len(argv) == 2:
        duplicates = {}
        if argv[1]:
            if os.path.isdir(argv[1]):
                if os.listdir(argv[1]):
                    files = os.listdir(argv[1])
                    if len(files) > 1:
                        for folder_path, _, files in os.walk(argv[1]):
                            for file in files:
                                file_path = os.path.join(folder_path, file)

                                file_hash =hashlib.sha256(open(os.path.join(folder_path, file), "rb").read()).hexdigest()
                                #print(file_hash)
                                if file_hash in duplicates:
                                    # if file hash already present in dictionary then add multiple list item to file_hash
                                    duplicates[file_hash].append(file_path)
                                    with open(folder_path+"\\"+"Log.txt", "a") as log_file:
                                        log_file.write(file + "\n")

                                else:
                                    # if file hash is not present in dictionary then add simple hash:file_path in dictionary
                                    duplicates[file_hash] = [file_path]


                                print(duplicates)


            else:
                print("Directory not found!")


if __name__ == "__main__":
    main()
