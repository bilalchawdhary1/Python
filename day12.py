# # List Methods in Python
# mylist = [10, 0, 1, 2, 3, 3, 4, 5]
# print(mylist)

# # 1 Insert an element at the end of the list
# mylist.append(6)
# print(mylist)

# # 2 Insert an element at a specific index
# mylist.insert(3, 7)
# print(mylist)

# # 3 Remove an element by value
# mylist.remove(10)
# print(mylist)

# # 4 Remove an element by index
# mylist.pop(2)
# print(mylist)

# # 5 Sort the list in ascending order
# mylist.sort()
# print(mylist)

# # 6 Sort the list in descending order
# mylist.sort()
# print(mylist)
# mylist.sort(reverse=True)
# print(mylist)

# # 7 Reverse the list
# mylist.reverse()
# print(mylist)

# # 8 Count the number of occurrences of a given element
# print(mylist.count(3))

# # 9 Get the index of the first occurrence of a given element
# print(mylist.index(3))

# # 10 Get the number of elements in the list
# print(len(mylist))
# print(mylist)

# # 11 Create a new list with unique elements from the original list
# mylist2 = [11, 45]
# mylist.extend(mylist2)
# # unique_list = list(set(mylist + mylist2))
# # unique_list = mylist + mylist2
# # print(unique_list)
# print(mylist)

# # l = [11, 45, 1, 2, 4, 6, 1, 1]
# # print(l)
# # l.append(7)
# # l.sort(reverse=True)
# # l.reverse()
# # print(l.index(1))
# # print(l.count(1))
# # m = l.copy()
# # m[0] = 0
# # l.insert(1, 899)
# # m = [900, 1000, 1100]
# # k = l + m
# # print(k)
# # l.extend(m)
# # print(l)

# # Tuples Methods in Python
# Python tuples are a type of data structure that is very similar to lists. The main difference between the two is that tuples are immutable, meaning they cannot be changed once they are created. This makes them ideal for storing data that should not be modified, such as database records.
tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if  3421 in tup:
  print("Yes 342 is present in this tuple")
tup2 = tup[1:4]
print(tup2)