# Which Number Is Not like the Others?
# Create a function that takes a list of numbers and
# return the number that's unique.


def unique(lst):
    dict = {}
    for item in lst:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 0
    for item in lst:
        if dict[item] == 0:
            return item


print(unique([3, 3, 3, 7, 3, 3]))  # ➞ 7

print(unique([0, 0, 0.77, 0, 0]))  # ➞ 0.77

print(unique([0, 1, 1, 1, 1, 1, 1, 1]))  # ➞ 0
