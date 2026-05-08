fd = open('demo.txt', 'r')
print("Information about file:", fd)
print("\nContents of File:")
print(fd.read())

print("Reading single line from file:", fd.readline())
print("\nCurrent File position is:", fd.tell())
fd.seek(0) #bring file cursor to initial position
print("Contents of whole file:")
print(fd.read())
fd.close()
fd = open('demo.txt', 'a')
fd.write('Hello World\n')
fd.write('Lorel Ipsum\n')
fd.seek(0)
#print(fd.read())
fd.close()

