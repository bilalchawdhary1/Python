# File Handling in Python
# File handling in Python is a powerful and versatile tool that can be used to perform a wide range of operations. However, it is important to carefully consider the advantages and disadvantages of file handling when writing Python programs, to ensure that the code is secure, reliable, and performs well.

# In this article we will explore Python File Handling, Advantages, Disadvantages and How open, write and append functions works in python file.

# Python File Handling
# Python supports file handling and allows users to handle files i.e., to read and write files, along with many other file handling options, to operate on files. The concept of file handling has stretched over various other languages, but the implementation is either complicated or lengthy, like other concepts of Python, this concept here is also easy and short.

# Python treats files differently as text or binary and this is important. Each line of code includes a sequence of characters, and they form a text file. Each line of a file is terminated with a special character, called the EOL or End of Line characters like comma {,} or newline character. It ends the current line and tells the interpreter a new one has begun. Let’s start with the reading and writing files.

# Advantages of File Handling in Python
# Versatility : File handling in Python allows you to perform a wide range of operations, such as creating, reading, writing, appending, renaming, and deleting files.
# Flexibility : File handling in Python is highly flexible, as it allows you to work with different file types (e.g. text files, binary files, CSV files , etc.), and to perform different operations on files (e.g. read, write, append, etc.).
# User – friendly : Python provides a user-friendly interface for file handling, making it easy to create, read, and manipulate files.
# Cross-platform : Python file-handling functions work across different platforms (e.g. Windows, Mac, Linux), allowing for seamless integration and compatibility.
# Disadvantages of File Handling in Python
# Error-prone: File handling operations in Python can be prone to errors, especially if the code is not carefully written or if there are issues with the file system (e.g. file permissions, file locks, etc.).
# Security risks : File handling in Python can also pose security risks, especially if the program accepts user input that can be used to access or modify sensitive files on the system.
# Complexity : File handling in Python can be complex, especially when working with more advanced file formats or operations. Careful attention must be paid to the code to ensure that files are handled properly and securely.
# Performance : File handling operations in Python can be slower than other programming languages, especially when dealing with large files or performing complex operations.
# For this article, we will consider the following ” geeks.txt ” file as an example.

#    1 Python File Open
# Before performing any operation on the file like reading or writing, first, we have to open that file.
# For this, we should use Python’s inbuilt function open() 
# but at the time of opening, we have to specify the mode, 
# which represents the purpose of the opening file.

file = open('filehandling.txt', 'r') # The 'r' mode is used for reading files. If the file does not exist, the open() function will raise an IOError.
# This will print every line one by one in the file
# text = file.read()
# print(text)
# file.close()
# for each in file:
#     print (each)
# Python code to illustrate with()
# with open("filehandling.txt") as file:  
#     data = file.read() 

# print(data)
with open('filehandling.txt') as file:
    # file.write('This is added line.')
    # file.write('\nThis is another added line.')
    # file.seek(0) # Move the cursor to the beginning of the file
    text = file.read()
print(text)
    # print(file.read())

# f = open('myfile.txt', 'r')
# i = 0
# while True:
#   i = i + 1
#   line = f.readline()
#   if not line:
#     break
#   m1 = int(line.split(",")[0])
#   m2 = int(line.split(",")[1])
#   m3 = int(line.split(",")[2])
#   print(f"Marks of student {i} in Maths is: {m1*2}")
#   print(f"Marks of student {i} in English is: {m2*2}")
#   print(f"Marks of student {i} in SST is: {m3*2}")

#   print(line)

f = open('myfile2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()
f = open('day25.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()
