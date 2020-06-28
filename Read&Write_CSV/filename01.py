def count_char(text, char):
    # count = 0
    # for c in text:
    #     if c == char:
    #         count += 1
    # return count
    # different way
    return text.count(char)


filename = input("Enter a filename: ")
with open(filename) as f:
    text = f.read()

# print(count_char(text, "r"))

# The next part of the program finds what percentage of the text
# each character of the alphabet occupies.

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))

# ===================================================

# Using dict

alph = "abcdefghijklmnopqrstuvwxyz"
letters = {}
count = 0
for c in text:
    if c.lower() in alph:
        letters[c] = letters.get(c, 0) + 1
        count += 1
for c in sorted(letters):
    print("{0} : {1}%".format(c, letters[c] / count * 100))

