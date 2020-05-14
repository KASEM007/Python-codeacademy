def end_zeros(num):
    new_num = str(num)
    count = len(new_num) - len(new_num.rstrip("0"))
    return count


print(end_zeros(0))  # == 1
print(end_zeros(1))  # == 0
print(end_zeros(10))  # == 1
print(end_zeros(101))  # == 0
print(end_zeros(245))  # == 0
print(end_zeros(100100))  # == 2
