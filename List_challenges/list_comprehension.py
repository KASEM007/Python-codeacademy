# List Comprehensions

# List comprehensions are a useful way of quickly creating lists
# whose contents obey a simple rule.
# For example, we can do the following:

# a list comprehension
cubes = [i ** 3 for i in range(5)]

print(cubes)
# Output
# >>> [0, 1, 8, 27, 64]


# a list comprehension, but changing the brackets to make the result a set:

cubes = {(i ** 3) for i in range(4)}
print(cubes)
print(type(cubes))

# you can create more than one element, like
# making a list of tuples...
cubes = [(i, i ** 3) for i in range(4)]
print(type(cubes[0]))

# ...and converting it into a dictionary
cubes = dict(cubes)
print(cubes)
