# Substring Between

# Write a function named substring_between_letters that takes a string named word,
# a single character named start, and another character named end.
# This function should return the substring between the first occurrence of
# start and end in word.
# If start or end are not in word, the function should return word.

# For example, substring_between_letters("apple", "p", "e") should return "pl".


def substring_between_letters(word, start, end):
    indx1 = word.find(start)
    indx2 = word.find(end)

    if indx1 == -1 or indx2 == -1:
        return word
    else:
        return word[indx1 + 1 : indx2]


# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"


# Answer explination:
# They are the same, except that str.find() returns -1 if the string is not found,
# and is only available for strings, while obj.index() throws an error if the argument
# is not found, and is available to lists and other subscriptable iterables.

# not takes precedence over or, so the expression is parsed as:
# if start or (end not in word):, and assuming that start is anything with a truth
# value of True (i.e. is not False, 0 (zero), an empty container
# (list,string, tuple, dictionary), or any expression that evalates to one of those),
# it will further parse to if True or anything_else:, which will always return True.

# The function print() evaluates the expression within its parentheses, and then sends
# the resulting value as a stream of text to the default i/o device, generally the screen.
# But (as with every Python function having no explicit return starement),
# it returns the value None.

# Remember:
# We print() values that we want to see

# We return values that Python needs to use
# (to assign to a variable, perhaps, or to send to another function.)
