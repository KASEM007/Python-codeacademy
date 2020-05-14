# Count Letters:

# Write a function called unique_english_letters that takes the string word as a parameter.
# The function should return the total number of unique letters in the string.
# Uppercase and lowercase letters should be counted as different letters.

# We’ve given you a list of every uppercase and lower case letter in the English alphabet.
# It will be helpful to include that list in your function.


def unique_english_letters(word):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    count = 0
    for char in letters:
        if char in word:
            count += 1
    return count


# Another Answer:
# def unique_english_letters(word):
#     letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# uniques = []
# for letter in word:
#     if letter in letters and not letter in uniques:
#         uniques.append(letter)
# return len(uniques)


# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
