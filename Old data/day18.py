# for Loop with else in Python

# Using else conditional statement with for loop in python
# In most of the programming languages (C/C++, Java, etc), the use of else 
# statement has been restricted with the if conditional statements.
#  But Python also allows us to use the else condition with for loops.

for i in range(0,10,2):
    print(i)
    # if i == 8:
    break
else:  # Executed because no break in for  # Not executed as there is a break
    print("No Break") 




# Python 3.x program to check if an array consists  
# of even number 
def contains_even_number(l): 
    for ele in l: 
        if ele % 2 == 0: 
            print ("list contains an even number") 
            break
  
    # This else executes only if break is NEVER 
    # reached and loop terminated after all iterations. 
    else:      
        print ("list does not contain an even number") 
  
# Driver code 
print ("For List 1:") 
contains_even_number([1, 9, 8]) 
print (" \nFor List 2:") 
contains_even_number([1, 3, 5]) 

# Using While Loop here's 
count = 0
while count < 10 :
    print(count)
    count += 1
    if count == 5:
        break
else:
    print("No Break")  # Not executed as there is a break

################ Exception Handling in Python ################
n = input("Enter the number : ")
print(f"Table of the {n} is:")

try:
    n = int(n)
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
except ValueError:
    print("Error: Please enter a valid number")

try:
    # Trying to divide a number by zero
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")