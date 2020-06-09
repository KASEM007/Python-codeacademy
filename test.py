def number_squaers(n):
    total = 0
    x = 1

    while total <= n:
        total += x * x
        if total == n:
            return total
        x += 1


# n - +1

# if total == n:
#     return n
# return -1


print(number_squaers(2))  # ➞ 5
print(number_squaers(4))  # ➞ 30
print(number_squaers(5))  # ➞ 55
