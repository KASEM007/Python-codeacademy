# def nearest_value(values, one):
#     for i in values:
#         if one in values:
#             return one
#         elif (one - 1 in values) and (one + 1 in values):
#             return one - 1
#         else:
#             if one + 1 in values:
#                 return one + 1


# print(nearest_value({4, 7, 10, 11, 12, 17}, 9))  # == 10
# print(nearest_value({4, 7, 10, 11, 12, 17}, 8))  # == 7
# print(nearest_value({4, 8, 10, 11, 12, 17}, 9))  # == 8
# print(nearest_value({4, 9, 10, 11, 12, 17}, 9))  # == 9
# print(nearest_value({4, 7, 10, 11, 12, 17}, 0))  # == 4
# print(nearest_value({4, 7, 10, 11, 12, 17}, 100))  # == 17
# print(nearest_value({5, 10, 8, 12, 89, 100}, 7))  # == 8
# print(nearest_value({-1, 2, 3}, 0))  # == -1

x = 10
print(abs(10))
