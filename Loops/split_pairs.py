# Split Pairs
# Split the string into pairs of two characters.
# If the string contains an odd number of characters,
# then the missing second character of the final pair
# should be replaced with an underscore ('_').


def split_pairs(a):
    new_lst = []

    if len(a) % 2 != 0:
        a += "_"

    for i in range(0, len(a), 2):
        new_lst.append(a[i : i + 2])
    return new_lst


print(split_pairs("abcd"))  # == ['ab', 'cd']
print(split_pairs("abc"))  # == ['ab', 'c_']
print(split_pairs("abcdf"))  # == ['ab', 'cd', 'f_']
print(split_pairs("a"))  # == ['a_']
print(split_pairs(""))  # == []
