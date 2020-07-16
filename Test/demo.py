def populate_list(list_to_populate=[], lenght=1):
    for num in range(lenght):
        list_to_populate.append(num)
    return list_to_populate

returned_list = populate_list(lenght=4)
print(returned_list)

returned_list = populate_list(lenght=6)
print(returned_list)
