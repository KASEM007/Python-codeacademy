# Largest Value
# Write a function named max_key that takes a dictionary named my_dictionary as a parameter.
# The function should return the key associated with the largest value in the dictionary.

# Write your max_key function here:
def max_key(my_dictionary):
    largest_value = float("-inf")
    largest_key = float("-inf")

    for keys, values in my_dictionary.items():
        if values > largest_value:
            largest_value = values
            largest_key = keys
    return largest_key


# Uncomment these function calls to test your  function:
print(max_key({1: 100, 2: 1, 3: 4, 4: 10}))
# should print 1
print(max_key({"a": 100, "b": 10, "c": 1000}))
# should print "c"
