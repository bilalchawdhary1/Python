 # Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode

# Example:
# hello world python
# Input: code
import random
import string

def generate_random_string(length=3):
    """Generate a random string of fixed length."""
    return ''.join(random.choices(string.ascii_lowercase, k=length))

messege = input("Please Enter The Message Here: ")
words = messege.split(" ")
coding = input("Enter 1 for Coding or 0 for Decoding: ")
coding = True if coding == "1" else False

if coding:
    cordmessege = []
    for word in words:
        if len(word) > 3:
            # Generate random prefix and suffix
            roundw1 = generate_random_string()
            roundw2 = generate_random_string()
            newmsg = roundw1 + word[1:] + word[0] + roundw2
            cordmessege.append(newmsg)
            print(f"Encoded '{word}' -> '{newmsg}'")
        else:
            cordmessege.append(word[::-1])
    print(" ".join(cordmessege))
else:
    decordmessege = []
    for word in words:
        if len(word) > 3:
            # Extract prefix and suffix (assume 3-character random strings)
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            decordmessege.append(stnew)
            print(f"Decoded '{word}' -> '{stnew}'")
        else:
            decordmessege.append(word[::-1])
    print(" ".join(decordmessege))


messege = input("Please Enter The Message Here's: ")
words = messege.split(" ")
coding = input("1 for Cording or 0 for Decording: ")
coding = True if (coding=="1") else False
# print(coding)
if(coding):
  cordmessege = []
  for word in words:
    if(len(word)>3):
      roundw1 = "fvc"
      roundw2 = "rny"
      newmsg = roundw1 + word[1:] + word[0] + roundw2
      cordmessege.append(newmsg)
    #   print(newmsg)
    else:
      cordmessege.append(word[::-1])
  print(" ".join(cordmessege))   
else:
  decordmessege = []
  for word in words:
    if(len(word)>=3):
      stnew = word[3:-3]
      stnew = stnew[-1] + stnew[:-1]
      decordmessege.append(stnew)
    else:
      decordmessege.append(word[::-1])
  print(" ".join(decordmessege))  


# st = input("Enter message: ")
# words = st.split(" ")
# coding = input("1 for Coding or 0 for Decoding: ")
# coding = True if (coding=="1") else False
# print(coding)
# if(coding):
#   nwords = []
#   for word in words:
#     if(len(word)>=3):
#       r1 = "dsf"
#       r2 = "jkr"
#       stnew = r1+ word[1:] + word[0] + r2
#       nwords.append(stnew)
#     else:
#       nwords.append(word[::-1])
#   print(" ".join(nwords))

# else:
#   nwords = []
#   for word in words:
#     if(len(word)>=3): 
#       stnew = word[3:-3]
#       stnew = stnew[-1] + stnew[:-1]
#       nwords.append(stnew)
#     else:
#       nwords.append(word[::-1])
#   print(" ".join(nwords))
