# Delete Starting Even Numbers

# Write a function called delete_starting_evens() that has a parameter named lst.
# The function should remove elements from the front of lst until the front of
# the list is not even. The function should then return lst.

# For example if lst started as [4, 8, 10, 11, 12, 15], then
# delete_starting_evens(lst) should return [11, 12, 15].

# Make sure your function works even if every element in the list is even!

#   ______Hint_____
# Use a while loop to check two things. First,
# check if the list has at least one element,
# using len(lst). Second, check to see if the
# first element is odd using mod (%). If both
# of those are True, slice off the first element
# of the list using lst = lst[1:].


# def delete_starting_evens(lst):
#     position = 0
#     for i in lst:
#         print(f"\nTesting position in original list {position} - Value: {i}")
#         if i % 2 == 0:
#             print(f"{i} is even - Getting rid of {lst[0]}")
#             lst = lst[1:]
#             print(f"New list: {lst}")
#         position += 1
#     return lst

############# Another Answer ############


def delete_starting_evens(lst):
    while lst and lst[0] % 2 == 0:
        lst.pop(0)
    return lst


# Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
