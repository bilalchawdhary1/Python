name = "Harry"
friend = "Rohan"
anotherFriend = 'Lovish'
apple = '''He said, 
Hi Harry
hey I am good
"I want to eat an apple'''
 
print("Hello, " + name)
# print(apple) 
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) # Throws an error
print("Lets use a for loop\n")
for character in apple:
    print(character)

fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
# print(fruit[0:4]) # including 0 but not 4
# print(fruit[1:4]) # including 1 but not 4
# print(fruit[:5])
# print(fruit[0:-3])
# print(fruit[:len(fruit)-3])
print(fruit[-1:len(fruit) - 3])
print(fruit[-3:-1])

# Quick Quiz:
# nm = "Harry"
# print(nm[-4:-2])
# @codewithharry

