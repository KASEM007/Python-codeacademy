# Recursion function


def clean_word(word):
    if len(word) == 1:
        return word
    print(f"print start function {word}")
    print("**********")
    if word[0] == word[1]:
        print(f"print before Condition {word}")
        print("**********")
        return clean_word(word[1:])
    print(f"print before Return {word}")
    print("**********")
    return word[0] + clean_word(word[1:])


print(clean_word("wwwooooorrrldd"))
print(clean_word("CCaalliiiiforrrniaaa"))
