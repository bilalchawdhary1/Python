from datetime import datetime

# print(datetime.now())
if(datetime.now().hour < 12):
    print("Good morning!")
elif(datetime.now().hour < 18):
    print("Good afternoon!")
else:
    print("Good evening!")