# for i in range(12):
#     if(i == 10):
#         break
#     print("5 X ", i+ 1 , "= ", 5 *(i + 1))

# for i in range (10):
#     print("2 X " , i+1  , "= " , 2* (i+1))
# break statement
# The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.
# example
# for i in range(1,101,1):
#     print(i ,end=" ")
#     if(i==50):
#         break
#     else:
#         print("Mississippi")
# print("Thank you")
# output
# 1 Mississippi
# 2 Mississippi
# 3 Mississippi
# 4 Mississippi
# 5 Mississippi
# .
# .
# .
# 50 Mississippi

# Continue Statement
# The continue statement skips the rest of the loop statements and causes the next iteration to occur.
# example
# for i in [2,3,4,6,8,0]:
#     if (i%2!=0):
#         continue
#     print(i)
# output
# 2
# 4
# 6
# 8
# 0
# Function in python 
def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

def isLesser(a, b):
  pass
  

a = 9
b = 8
isGreater(a, b)
calculateGmean(a, b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)
c = 8
d = 74
isGreater(c, d)
calculateGmean(c, d)
# gmean2 = (c*d)/(c+d)
# print(gmean2)
def MyName(name):
  print("name",name)

MyName("Muhammad Bilal")
MyName("Muhammad Rehan")
MyName("Muhammad Waqas")