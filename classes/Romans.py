class Romans:
    def __init__(self):
        self._number = None  # Private field. It does not call the setter!

    # Define the getter
    # @property
    def number(self):
        return self._number

    # Define the setter

    # @number.setter
    def number(self, value):
        if value >= 1 and value <= 5:
            self._number = value
        else:
            raise ValueError("Number not recognized")

    # Define the getter
    # @property
    def roman(self):
        number_2_roman = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V"}
        return number_2_roman[self._number]

    # Define the setter
    # @roman.setter
    def roman(self, value):
        roman_2_number = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5}

        if value in roman_2_number:
            self._number = roman_2_number[value]
        else:
            raise ValueError("Roman numeral not recognized")


x = Romans()

x.number = 3
print(x.number)  # it display: 3
print(x.roman)  # it display: III

x.roman = "V"
print(x.number)  # it display: 5
print(x.roman)  # it display: V

