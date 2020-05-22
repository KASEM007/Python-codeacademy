alpha = "abcdefghijklmnobqrstuvwxyz"
punctuation = "., ?, !"
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
translate_message = ""

# for char in message:
#     if char not in punctuation:
#         char_idx = alpha.find(char)
#         translate_message += alpha[(char_idx + 10) % 26]
#     else:
#         translate_message += char

# print(translate_message)

for char in message:
    if char in punctuation:
        translate_message += char
    else:
        char_idx = alpha.find(char)
        translate_message += alpha[(char_idx + 10) % 26]
print(translate_message)
