# Map, Filter and Reduce in Python 

    # Map function in Python:
    # The map() function applies a given function to all items of an iterable (list, tuple etc.) and returns a list of the results.
    # Syntax: map(function, iterable)
    # Example:

    # Filter function in Python:
    # The filter() function filters elements of an iterable (list, tuple etc.) based on a function and returns a new iterable.
    # Syntax: filter(function, iterable)
    # Example:
list_numbers = [1, 2, 3, 4, 5]
map_list = list(map(lambda x: x * 2, list_numbers))

print(map_list)

# filter in python 

filter_list = list(filter(lambda x: x % 2 == 0, list_numbers))

print(filter_list)

# Reduce function in Python:
    # The reduce() function applies a given function of two arguments cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single output.
    # Syntax: reduce(function, iterable)
    # Example:

from functools import reduce

reduce_list = reduce(lambda x, y: x + y, list_numbers)

print(reduce_list)

# map(), filter(), and reduce() functions are built-in functions in Python. 
# They are used in conjunction with lambda functions to perform specific operations on iterable data.




# is and "==" in python 

# The "is" operator checks if two objects are identical (point to the same memory location).
# The "==" operator checks if the values of two objects are equal.
# Example:
a = 10
b = 10

print(a is b) # True

print(a == b) # True

# The "is" operator is faster than the "==" operator because it doesn't need to compare the values of the objects, but rather checks if they are located at the same memory location.

# Generators in Python

    # Generators are a type of iterable, like lists or tuples. Unlike lists, they don't allow indexing, but they can still be iterated through with for loops.
    # Generators are created using functions and the yield statement.
    # Syntax: def function_name(): yield expression
    # Example:
    # def generate_numbers():
    #     for i in range(1, 11):
    #         yield i
    # generator = generate_numbers()
    # for num in generator:
    #     print(num)