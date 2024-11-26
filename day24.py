# Global and Local Variables in Python
# Last Updated : 25 Jul, 2024
# Python Global variables are those which are not defined inside any function and have a global scope whereas Python local variables are those which are defined inside a function and their scope is limited to that function only. In other words, we can say that local variables are accessible only inside the function in which it was initialized whereas the global variables are accessible throughout the program and inside every function. 

# Python Local Variables
# Local variables in Python are those which are initialized inside a function and belong only to that particular function. It cannot be accessed anywhere outside the function. Let’s see how to create a local variable.

# Creating local variables in Python
# Defining and accessing local variables

def f():
    # local variable
    s = "I love Allah"
    print(s)
# Driver code
f()
def f():
    
    # local variable
    s = "I love Geeksforgeeks"
    print("Inside Function:", s)

# Driver code
f()
# print(s) print show error =  NameError: name 's' is not defined

# This function uses global variable s
def f():
    print("Inside Function", s)

# Global scope
s = "I love Allah"
f()
print("Outside Function", s)