# Accept file name and one string from user and return the frequency of that string from file.
# Input : Demo.txt Lorem
# Search “Lorem” in Demo.txt

#option 1
fd = open("abc.txt","r")
print(fd.read())

ipstr = input("Enter a string")
print(ipstr)

with open("abc.txt","r") as file:
    content = file.read()
    count = content.count(ipstr)

print("No of occurrences in file :", count)


#option 2

count1=0
with open("abc.txt","r") as file:
    for line in file:
        count1 += line.count(ipstr)

print("Total occurrences in file :", count1)