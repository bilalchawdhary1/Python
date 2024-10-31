# 10/31/24 Today how to make simple calculator with python
operator = input("Enter an operator here (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2st number: "))

if operator == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operator == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operator == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Cannot divide by zero.")