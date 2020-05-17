alpha = "abcdefghijklmnobqrstuvwxyz"
punctuation = "., ?, !"
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
translate_message = ""


alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
translated_message = ""
# for letter in message:
#     if letter not in punctuation:
#         letter_value = alphabet.find(letter)
#         translated_message += alphabet[(letter_value + 10) % 26]
#     else:
#         translated_message += letter
# print(translated_message)

for letter in message:
    if letter not in punctuation:
        letter_idx = alpha.find(letter)
        translate_message += alpha[(letter_idx + 10) % 26]
    else:
        translate_message += letter

print(translate_message)
