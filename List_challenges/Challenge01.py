# **************************** tenth_power **********************************#

# Write a function named tenth_power() that has one parameter named num.
# The function should return num raised to the 10th power.

# Write your tenth_power function here:
def tenth_power(num):
    return num ** 10


# Uncomment these function calls to test your tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

# **************************** Square Root **********************************#
# 2. Square Root

# Write a function named square_root() that has one parameter named num.
# Use exponents (**) to return the square root of num.

# Write your square_root function here:
def square_root(num):
    return num ** 0.5


# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

# ****************************** Win Percentage ********************************#

# 3. Win Percentage
# Create a function called win_percentage() that takes two parameters named wins and losses.
# This function should return out the total percentage of games won
# by a team based on these two numbers.

# Write your win_percentage function here:
def win_percentage(wins, losses):
    total = wins + losses
    return (100 * wins) / total


# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100

# ****************************** First Three Multiples ********************************#

# 1. First Three Multiples

# Write a function named first_three_multiples() that has one parameter named num.
# This function should print the first three multiples of num. Then, it should
# return the third multiple.
# For example, first_three_multiples(7) should print 7, 14, and 21 on three
# different lines, and return 21.

# Write your first_three_multiples function here:

# def first_three_multiples(num):
#   print(num)
#   print(num*2)
#   print(num*3)
#   return num*3
###################### Another answer###############
def first_three_multiples(num):
    for i in range(1, 4):
        print(num * i)
    return num * i


# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0

# ******************************** Tip ******************************#

# 2- Tip

# Create a function called tip() that has two parameters named total and percentage.
# This function should return the amount you should tip given a total
# and the percentage you want to tip.

# Write your tip function here:
def tip(total, percentage):
    return total * (percentage / 100)


# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

# ******************************** All Operations ******************************#

# 3- All Operations

# Create a function named lots_of_math(). This function should have four parameters
# named a, b, c, and d. The function should print 3 lines and return 1 value.
# First, print the sum of a and b. Second, print d subtracted from c.
# Third, print the first number printed, multiplied by the second number printed.
# Finally, return the third number printed mod a.

# Write your lots_of_math function here:
def lots_of_math(a, b, c, d):
    ab = a + b
    print(ab)
    dc = c - d
    print(dc)
    print(ab * dc)
    return (ab * dc) % a


# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0
