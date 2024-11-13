# Python Docstrings
def square(n):
    """This function takes an integer n as input and returns the square of n."""
    return n**2

# Accessing the docstring
print(square(10))
print(square.__doc__)  # Prints: This function takes an integer n as input and returns the square of n.

def my_function():
    ' ' 'Demonstrates triple double quotes docstrings and does nothing really' ' '
 
    return None

print("Using __doc__:")
print(my_function.__doc__)

print("Using help:")
help(my_function)

# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1


# factorial(n) = n * factorial(n-1)
def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)


print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1

# Quick Quiz: Write a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

# 0 1 1 2 3 5 8....
def fibonacci(number):
    if number < 0:
        print("Input should be a non-negative integer")
    elif number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

# Testing the function
print(fibonacci(0))  # Output: 0
print(fibonacci(9))  # Output: 34
print(fibonacci(10)) # Output: 55

