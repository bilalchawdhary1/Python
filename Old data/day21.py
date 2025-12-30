# Virtual Environment in Python 
# What is a Virtual Environment?
# A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated Python virtual environments for them. This is one of the most important tools that most Python developers use.

# Why do we need a virtual environment?
# Imagine a scenario where you are working on two web-based Python projects one of them uses Django 4.0 and the other uses Django 4.1 (check for the latest Django versions and so on). In such situations, we need to create a virtual environment in Python that can be really useful to maintain the dependencies of both projects.

# When and where to use a virtual environment?
# By default, every project on your system will use these same directories to store and retrieve site packages (third-party libraries).

# How does this matter? Now, in the above example of two projects, you have two versions of Django. This is a real problem for Python since it can’t differentiate between versions in the “site-packages” directory. So both v1.9 and v1.10 would reside in the same directory with the same name.

# from math import sqrt, pi
# from math import pi, sqrt as s
# import math as math_builtin_python

# result = math_builtin_python.sqrt(9) * math_builtin_python.pi
# print(result)  # Output: 3.0

# from harry import welcome, harry
import harry as hr
import math

print(dir(math))
print(math.nan, type(math.nan))
hr.welcome()
print(hr.harry)