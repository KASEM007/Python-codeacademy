# Large Sum

# Create a function named larger_sum() that takes two lists of numbers
# as parameters named lst1 and lst2.
# The function should return the list whose elements sum to the greater
# number. If the sum of the elements of each list are equal, return lst1.

# Write your function here
def larger_sum(lst1, lst2):
    sum_lst1 = 0
    sum_lst2 = 0
    for i in range(len(lst1)):
        sum_lst1 += lst1[i]

    for i in range(len(lst2)):
        sum_lst2 += lst2[i]

    if sum_lst1 > sum_lst2:
        return lst1
    elif sum_lst2 > sum_lst1:
        return lst2
    else:
        return lst1


# Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

