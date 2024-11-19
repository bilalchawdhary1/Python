# Try, Except, else and Finally in Python

# try:
#        # Some Code.... 
# except:
#        # optional block
#        # Handling of exception (if required)
# else:
#        # execute if no exception
# finally:
#       # Some code .....(always executed)


def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)

# Python code to illustrate working of try()  
def divide(x, y): 
    try: 
        # Floor Division : Gives only Fractional
        # Part as Answer 
        result = x // y 
        print("Yeah ! Your answer is :", result) 
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ") 
  
# Look at parameters and note the working of Program 
divide(3, 2) 
divide(3, 0)

# Catch Multiple Exceptions in Python
# Here’s an example that demonstrates how to use multiple except clauses to handle different exceptions:

try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {e}")