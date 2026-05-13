# Write a program which accept two file names from user and compare contents of both the
# files. If both the files contains same contents then display success otherwise display failure.
# Accept names of both the files from command line.
# Input : demo.txt abc.txt
# Compare contents of demo.txt and abc.txt

import filecmp

filename1 = input("Enter first file name: ")
filename2 = input("Enter second file name: ")

if filecmp.cmp(filename1, filename2, shallow=True):
    print("Source Files match")
else:
    print("Source Files not match")



