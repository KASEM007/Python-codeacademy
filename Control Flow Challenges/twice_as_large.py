# ******************************** Twice As Large ******************************#

# Create a function named twice_as_large() that has two parameters
# named num1 and num2.
# Return True if num1 is more than double num2. Return False otherwise.

# Write your twice_as_large function here:
def twice_as_large(num1, num2):
    new_num = num1 / 2
    if new_num > num2:
        return True
    else:
        return True


# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True
