# ON\OFF Switch

# Create a function that returns how many possible
# outcomes can come from a certain number of switches
# (on / off).


def pos_com(num):
    return 2 ** num


print(pos_com(1))  # ➞ 2
print(pos_com(3))  # ➞ 8
print(pos_com(10))  # ➞ 1024

# 2**3 == 8 && 3**2 == 9
