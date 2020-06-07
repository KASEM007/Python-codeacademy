# Uniocode
# translate the string to unicode listpygame.examples.aliens.main()


def test_func(str):
    unicod = []
    for i in str:
        unicod.append(ord(i))
    # print(unicod)
    return unicod


def testfunc2(unicod):
    new_str = ""
    for i in unicod:
        new_str += chr(i)
    return new_str


print(test_func("I love python"))
print("__________\n")
print(test_func("Mohamed"))
print("__________\n")
print(testfunc2([77, 111, 104, 97, 109, 101, 100]))
