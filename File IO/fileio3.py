# Write a program which accept file name from user and create new file named as abc.txt and copy all contents from existing file into new file. Accept file name through command line arguments.
# Input : demo.txt
# Create new file as abc.txt and copy contents of demo.txt in abc.txt

import os

print("Enter file name: ")
filename = input()
if os.path.isfile(filename):
    with open(filename, 'r') as src, open('abc.txt', 'w') as dst:
        dst.write(src.read())
        
else:
    print("Source File not exists")


