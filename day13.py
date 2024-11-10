mytuple = (1, 2, 76, 342, 32, "green", True)

tolist = list(mytuple)
tolist.append(15)
tolist.pop(5)
print(tolist)

mytuple =  tuple(tolist)
print(mytuple)