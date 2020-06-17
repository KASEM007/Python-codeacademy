# list with duplicate values

list1 = [1, 2, 5, 6, 7, 8, 4, 2, 1, 4, 6]

# create empty list object
list2 = []

[list2.append(item) for item in list1 if item not in list2]

print(list2)
