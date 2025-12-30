# Function Arguments in Python
# def average(a, b, c=1):
#   print("The average is ", (a + b + c) / 2)

# def average(*numbers):
  # print(type(numbers))
#   sum = 0
#   for i in numbers:
    # sum = sum + i
  # print("Average is: ", sum / len(numbers))
  # return 7
#   return sum / len(numbers)
# average(4, 6)
# average(b=9)
# c = average(5, 6, 7, 1)
# print(c)
# def name(**name):
#   # print(type(name))
#   print("Hello,", name["fname"], name["mname"], name["lname"])
# name(mname="Buchanan", lname="Barnes", fname="James")

# 1 Function Argument
def avrange(a,b):
    return (a + b) / 2

average = avrange(2,4)
print(average)

# 2 Function Argument with Default Values
def avrange2( a = 4, b = 5):
    return (a + b) / 2

average2 = avrange2()
average2 = avrange2(2,2)
average2 = avrange2(a=10)
average2 = avrange2(b=12)
print(average2)

# 3 Variable Length Arguments
# Python Function With Arbitrary Arguments
def var_args(*args):
    print("Number of arguments:", len(args))
    for arg in args:
        print("Argument:", arg)

var_args("Hello", "World", 123, True, [1,2,3])

# 4 Keyword Arguments
def key_args(**kwargs):
    print("Number of key arguments:", len(kwargs))
    for key, value in kwargs.items():
        print(f"Key: {key}, Value: {value}")    

key_args(name="John", age=30, city="New York")

# 5 Arbitrary Keyword Arguments 
def arbitrary_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

arbitrary_args(1, 2, 3, name="John", age=30, city="New York")

# 6 Nested Function Arguments
def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)

result = outer_function(2, 3)
print(result)
