# Stressful subj

# The function should recognise if a subject line is stressful.
# A stressful subject line means that all letters are in uppercase,
# and/or ends by at least 3 exclamation marks, and/or contains at
# least one of the following “red” words: "help", "asap", "urgent".
# Any of those "red" words can be spelled in different ways -
# "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P",
# even in a very loooong way "HHHEEEEEEEEELLP,"
# they just can't have any other letters interspersed between them.

################ Best Answer #######################
def is_stressful(subj):
    for word in ("help", "asap", "urgent"):
        s = "".join(x for x in subj.lower() if x in word + " ")
        for i in s * len(s):
            s = s.replace(i + i, i)
        if s.count(word):
            return True
    return subj == subj.upper() or subj.endswith("!!!")


#################### Another Answer ################
# import re
# def is_stressful(subj):

#     if subj.isupper():
#         return True
#     if subj.endswith("!!!"):
#         return True
#     for word in subj.lower().split():
#         for red_word in ["help", "asap", "urgent"]:
#             if re.search("+[^0-9a-z]*".join(red_word), word) is not None:
#                 return True
#     return False

################ Another Answer #####################


# def is_stressful(subj):
#     if subj[-3:] == "!!!":
#         return True
#     subject, char = "", ""
#     isAllUpper = True
#     for x in subj:
#         if x.isalpha():
#             if x.islower():
#                 isAllUpper = False
#             x = x.lower()
#             if char != x:
#                 subject += x
#                 char = x
#     if isAllUpper:
#         return True
#     if "help" in subject or "asap" in subject or "urgent" in subject:
#         return True
#     return False


################# Another Answer ####################


# def is_stressful(subj):

#     if subj.isupper() is True:  # check all chracters are Upper
#         return True

#     if subj[-3:] == "!!!":  # check that given string not ending to '!!!'
#         return True

#     alfa = ""
#     num = 0
#     for i in subj:
#         if i.isalpha() != True and i != " ":  # dell all not alfa characters
#             subj = subj.replace(i, "")
#         elif i == alfa:  # check to alfa
#             num += 1  # count repeated character
#         else:
#             if num > 0:  # dell repeated characters
#                 subj_1 = subj[: subj.index(i) - num] + subj[subj.index(i) :]
#                 subj = subj_1
#             alfa = i
#             num = 0
#     subj = subj.lower()  # transform to low register
#     alert = ["help", "asap", "urgent"]  # alert string
#     for j in alert:  # compare all words in given string with alert words
#         if subj.find(j) != -1:
#             return True
#     return False


print(is_stressful("UUUURGGGEEEEENT here"))  # True
print(is_stressful("Hi"))  # == False, "First"
print(is_stressful("I neeed HELP"))  # == True, "Second"
