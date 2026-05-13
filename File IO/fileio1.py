# Write a program which accepts file name from user and check whether that file exists in current directory or not.
# Input : Demo.txt
# Check whether Demo.txt exists or not.

from pathlib import Path
import os
print("Enter file name to check if file exits or not.")
filepath = Path(input())

if filepath.is_file():
    print("File exists")
else:
    print("File not exists")

#using traditional method
if os.path.isfile(filepath):
    print("File exists in current directory")
else:
    print("File not exists")

