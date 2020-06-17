import csv

with open("addresses.csv", newline="") as addresses_csv:
    address_reader = csv.DictReader(addresses_csv, delimiter=";")
    for row in address_reader:
        print(row["Address"])


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

import csv

with open("books.csv", newline="") as books_csv:
    books_reader = csv.DictReader(books_csv, delimiter="@")
    isbn_list = []
    for row in books_reader:
        isbn_list.append(row["ISBN"])

