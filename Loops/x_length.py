# X Length
# Create a function called x_length_words that takes a string named
# sentence and an integer named x as parameters.
# This function should return True if every word in sentence has a
# length greater than or equal to x.

# Write your x_length_words function here:
# def x_length_words(sentence, x):
#     new_sent = sentence.split()
#     for i in range(len(new_sent)):
#         if len(new_sent[i]) < x:
#             return False
#         else:
#             return True

############################### Better Answer #########################


def x_length_words(sentence, x):
    for word in sentence.split():
        if len(word) < x:
            return False
    return True


# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
