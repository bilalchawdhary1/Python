import time
current_hour  = int(time.strftime('%H'))
if 5 <= current_hour < 12 :
    print("Good Morning!")
elif 12 <= current_hour < 18 :
    print("Good Afternoon!")
elif 18 <= current_hour < 21 :
    print("Good Evening!")
else :
    print("Good Night!")

# https://docs.python.org/3/library/time.html#time.strftime

# Morning: 5 AM to 11:59 AM.
# Afternoon: 12 PM to 5:59 PM.
# Evening: 6 PM to 8:59 PM.
# Night: 9 PM to 4:59 AM.

# - Match Case

x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")
    case 5:
        print("case is 5")
    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)