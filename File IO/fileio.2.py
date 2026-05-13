# Write a program which accept file name from user and open that file and display the contents of that file on screen.
# Input : Demo.txt
# Display contents of Demo.txt on console.

import os

print("Enter file name:\n")
fname = input()
if os.path.isfile(fname):
    fd = open(fname,'r')
    print(fd.read())
    fd.close()
else:
    print("File not exists")

