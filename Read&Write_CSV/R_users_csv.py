import os
import csv

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

list_of_email_addresses = []
list_of_users_names = []

with open("users.csv", newline="") as users_csv:
    user_reader = csv.DictReader(users_csv)
    for row in user_reader:
        list_of_email_addresses.append(row["Email"])
        list_of_users_names.append(row["Username"])

print(list_of_email_addresses)
print(list_of_users_names)
