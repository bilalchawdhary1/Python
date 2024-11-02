# In Python, typecasting (or type conversion) is a way to change the data type of a variable from one type to another. Python supports several built-in functions for explicit typecasting: 
# 1. int()
# Converts a value to an integer.
# Usage: int(3.5) returns 3
a = "123"
b = int(a)  # Converts string "123" to integer 123

# 2. float()
# Converts a value to a floating-point number.
# Usage: float("3.5") returns 3.5
a = "12.34"
b = float(a)  # Converts string "12.34" to float 12.34

# 3. str()
# Converts a value to a string.
# Usage: str(3.5) returns "3.5"
a = 123
b = str(a)  # Converts integer 123 to string "123"

# 4. bool()
# Converts a value to a Boolean.
# Usage: bool(0) returns False, bool(1) returns True
a = 0
b = bool(a)  # Converts integer 0 to Boolean False
a = 1
b = bool(a)  # Converts integer 1 to Boolean True

# 5. list(), tuple(), set()
# Converts a value to a list, tuple, or set respectively.
a = "hello"
b = list(a)   # Converts string "hello" to ['h', 'e', 'l', 'l', 'o']
c = tuple(a)  # Converts string "hello" to ('h', 'e', 'l', 'l', 'o')
d = set(a)    # Converts string "hello" to {'h', 'e', 'l', 'o'}

# 6. dict()
# Converts a sequence of key-value pairs to a dictionary.
a = [("name", "Alice"), ("age", 25)]
b = dict(a)  # Converts list of tuples to dictionary {'name': 'Alice', 'age': 25}

# Implicit Typecasting
# In some cases, Python does implicit typecasting, such as when adding an integer to a float:
a = 5      # int
b = 3.2    # float
c = a + b  # Python automatically converts `a` to float
print(c)   # Output: 8.2 (float)

