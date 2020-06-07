tarot = {
    1: "The Magician",
    2: "The High Priestess",
    3: "The Empress",
    4: "The Emperor",
    5: "The Hierophant",
    6: "The Lovers",
    7: "The Chariot",
    8: "Strength",
    9: "The Hermit",
    10: "Wheel of Fortune",
    11: "Justice",
    12: "The Hanged Man",
    13: "Death",
    14: "Temperance",
    15: "The Devil",
    16: "The Tower",
    17: "The Star",
    18: "The Moon",
    19: "The Sun",
    20: "Judgement",
    21: "The World",
    22: "The Fool",
}

# spread = {}
# spread["past"] = tarot.pop(13)
# spread["present"] = tarot.pop(22)
# spread["future"] = tarot.pop(10)

# for key, value in spread.items():
#     print("Your " + key + " is the " + value + " card" + ".")

########################################
# You can try to write the code on your own, here are some tips:

# We need numpy.py - we’ve used this library before. We can bring its
# functionality into our program with a command: import numpy as np .
# As a reminder numpy is a mathematic library with a bunch of useful functions.
# numpy.random.choice() will be the most suitable option to choose the card.
# It takes a list of numbers and returns a random choice from that list.
# In order to retreive each card will need to use the list of all
# available card indices, which hold all the currently present keys in the
# tarot list as an argument for np.random.choice().
# Convenient for us, once the card is ‘popped’ it disappears from the list
# together with its index, and if we update the list each time
# np.random.choice() won’t consider that index again.
# If you’re stuck somewhere or it’s too difficult here’s the code:

import random


def tarot_card():
    spread = {}
    spread["past"] = tarot.pop(random.choice(list(tarot)))
    spread["present"] = tarot.pop(random.choice(list(tarot)))
    spread["future"] = tarot.pop(random.choice(list(tarot)))

    for key, value in spread.items():
        print("Your " + key + " is the " + str(value) + " card.")


tarot_card()
