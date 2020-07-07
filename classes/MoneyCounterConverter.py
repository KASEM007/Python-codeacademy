import math
class MoneyCounter():
    def __init__(self, pennis):
        self.dollar = math.floor(pennis/100)
        self.cents = pennis % 100
        self.pennis = pennis

    def __add__(self, other):
        return MoneyCounter(self.pennies + other.pennies)

    def print(self):
        print('$', self.dollar, '.',self.cents)

mc = MoneyCounter(150)
mc.print()
mc2 = MoneyCounter(260)
mc2.print()
##mc3 = mc + mc2
##mc3.print()
