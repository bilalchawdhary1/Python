# seek(), tell() and other functions
# seek() method
# In Python, seek() function is used to change the position of the File Handle to a given specific position. 
# File handle is like a cursor, which defines from where the data has to be read or written in the file. 
with open('day25.txt' , 'r') as f:
    f.seek(5) # Move the cursor to the 6th position
    print(f.tell()) # Print the current position
    print(f.readline()) # Read the next line
    # we aslo use read mothod to defile how many character we want to read 
    # f.seek(0) # Move the cursor to the beginning of the file
    # print(f.tell()) # Print the current position
    # print(f.read(10)) # Read the next 10 characters

# truncate function 
                    # It removes the content from the current position to the end of the file. 
with open('day25.txt' , 'r+') as f:
    f.truncate(10) # Remove the content from the 11th position to the end of the file
    print(f.read()) # Read the content after truncation

# with statement in Python
                    # A 'with' statement simplifies the management of resources, such as file handles.
                    # It ensures that resources are properly closed after they are no longer needed.
                    # The with statement guarantees that the file is closed even if an exception occurs.
                    # The 'with' statement is used for opening a file and performing operations on it.
                    # Here's an example of using the 'with' statement to open and read a file:
                    # with open('example.txt', 'r') as file:
                    #     content = file.read()
                    #     print(content)
# write file 
                    # The write() method is used to write data to a file.
                    # It takes a string as an argument and writes it to the file.
                    # If the file does not exist, it will be created.
                    # If the file exists, the data will be appended to the end of the file.
with open('day26.txt' , 'a') as f:
    f.write('This is a new line.\n') # Write the string to the file

# write with w argument
                    # The 'w' argument in the open() function will overwrite the existing content in the file.
                    # If the file does not exist, it will be created.
                    # If the file exists, the existing content will be deleted.
with open('day26.txt', 'w') as f:
    f.write('This is a new content.\n') # Write the string to the file 
    

# Lambda functions in Python
                    # A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.
                    # It is defined using the lambda keyword.
                    # The syntax for a lambda function is: lambda arguments: expression
                    # Here's an example of a lambda function that adds two numbers:
                    # add = lambda x, y: x + y
                    # print(add(3, 5))  # Output: 8
s = 'muhammadbilal'

upper = lambda string: string.upper()
print(upper(s))

def cube(y):
    return y*y*y

lambda_cube = lambda y: y*y*y
print("Using function defined with `def` keyword, cube:", cube(5))
print("Using lambda function, cube:", lambda_cube(5))

# we salo use lamda function as argument 
                    # In the following example, we use a lambda function as an argument to the sort() function.
                    # The lambda function takes a tuple (name, age) as an argument and returns the age.
                    # The sort() function then uses this lambda function to sort the list of tuples by age.
people = [('Alice', 25), ('Bob', 30), ('Charlie', 28)]
people.sort(key=lambda x: x[1])
print(people)

def appl(fx, value):
  return 6 + fx(value)

cube = lambda x: x * x * x
print(cube(5))
print(appl(lambda x: x * x , 2))

