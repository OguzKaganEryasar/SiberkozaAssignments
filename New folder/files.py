# Python has functions for creating, reading, updating, and deleting files.

#Open a file
myFile_oke = open('myfile_oke.txt', 'w')

# Get some info
print('Name: ', myFile_oke.name)
print('Is Closed : ', myFile_oke.closed)
print('Opening Mode: ', myFile_oke.mode)

# Write to file
myFile_oke.write('I love Python')
myFile_oke.write(' and JavaScript')
myFile_oke.close()

# Append to file
myFile_oke = open('myFile_oke.txt', 'a')
myFile_oke.write(' I also like PHP')
myFile_oke.close()

# Read from file
myFile_oke = open('myfile.txt', 'r+')
text_oke = myFile_oke.read(100)
print(text_oke)