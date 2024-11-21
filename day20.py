# Short hand if else statements
a = 20
b = 40

if a < b:
    smaller = a
    larger = b
    # print("The smaller number is", smaller)
    # print("The larger number is", larger)


# Ternary operator
smaller = a if a < b else b
larger = a if a > b else b
# print("The smaller number is", smaller)
# print("The larger number is", larger)
# in js
# let gender = isMale ? 'Male' : 'Female';
# in python 
gender = input("Enter Your Gender(M/F) Here: ")
print("You're Mail") if (gender == "m") else print("You're Female") if (gender == "f") else print("Please Enter Valid Gender")
# print("a smaller") if a < b else print("a larger")

a = 330
b = 330
# print("A") if a > b else print("=") if a == b else print("B")

# Enumerate Function in Python
l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
# for ele in enumerate(l1):
    # print (ele)

# changing index and printing separately
# for count, ele in enumerate(l1, 1):
    # print (count, ele)

# numbers = [1,2,3,4,5,6,7]

# printing the tuples in object directly
# for number in numbers:
    # print(number)

# changing index and printing separately

# for i, number in enumerate(numbers, 1):
    # print(i, number)


#     Enumerate() in Python
# Last Updated : 25 Jul, 2024
# Often, when dealing with iterators, we also need to keep a count of iterations. Python eases the programmers’ task by providing a built-in function enumerate() for this task. The enumerate () function adds a counter to an iterable and returns it in the form of an enumerating object. This enumerated object can then be used directly for loops or converted into a list of tuples using the list() function.

#  Syntax:  enumerate(iterable, start=0) 


#  Parameters: 


#  Iterable:  any object that supports iteration 
#  Start:  the index value from which the counter is to be started, by default it is 0 
#  Return:  Returns an iterator with index and element pairs from the original iterable 


# Example

# Here, we are using the enumerate() function with both a list and a string. Creating enumerate objects for each and displaying their return types. It also shows how to change the starting index for enumeration when applied to a string, resulting in index-element pairs for the list and string .