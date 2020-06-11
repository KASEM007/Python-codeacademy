def disemvowel(string):
    #     new_string = ""
    #     vowels = "aeouiAEOUI"

    #     for i in string:
    #         if i in vowels:
    #             continue
    #         else:
    #             new_string += i

    #     return new_string

    # print(disemvowel("This website is for losers LOL!"))
    # "Ths wbst s fr lsrs LL!")

    ########## Another answer ###########

    return "".join(c for c in string if c not in "aeiouAEIOU")


print(disemvowel("This website is for losers LOL!"))  # "Ths wbst s fr lsrs LL!"
