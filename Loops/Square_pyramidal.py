# Square pyramidal number (Sum of Squares):

# A Square pyramidal number represents sum of squares of first natural
# numbers. First few Square pyramidal numbers
# are 1, 5, 14, 30, 55, 91, 140, 204, 285, 385, 506, …

# Geometrically these numbers represent number of spheres to be stacked
# to form a pyramid with square base.
# Please see this Wiki image for more clarity.
# Given a number s (1 <= s <= 1000000000).
# If s is sum of the squares of the first n natural
# numbers then print n, otherwise print -1.

# Examples :

# Input : 14
# Output : 3
# Explanation : 1*1 + 2*2 + 3*3 = 14
# Input : 26
# Output : -1


def number_squaers(n):
    sum = 0
    for i in range(0, n + 1):
        sum += i * i  # or i**2
    return sum


print(number_squaers(2))  # ➞ 5
print(number_squaers(4))  # ➞ 30
print(number_squaers(5))  # ➞ 55
