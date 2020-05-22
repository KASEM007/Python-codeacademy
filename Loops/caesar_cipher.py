# alpha = "abcdefghijklmnobqrstuvwxyz"
# punctuation = "., ?, !"
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
# translate_message = ""


def decoder_message(message, offset):
    alpha = "abcdefghijklmnobqrstuvwxyz"
    translate_message = ""

    for char in message:
        if char not in alpha:
            translate_message += char
        else:
            char_idx = alpha.find(char)
            translate_message += alpha[(char_idx + offset) % 26]
    return translate_message


print(decoder_message(message, 10))


############################## decoded Message ##############################

# message = "This will feel great when it works, I feel like a spy, james bond, man with a plan and license to kill lol."


# def decoded_message(message, offset):
#     alpha = "abcdefghijklmnobqrstuvwxyz"
#     translate_message = ""
#

#     for char in message:
#         if char not in alpha:
#             translate_message += char
#         else:
#             char_idx = alpha.find(char)
#             translate_message += alpha[(char_idx - offset) % 26]

#     return translate_message


# print(decoded_message(message, 5))

#################### coded caser cipher without knowing the shift value ########################

coded_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
for i in range(0, 26):
    print("offset: " + str(i))
    print("\t " + decoder_message(coded_message, i) + "\n")
