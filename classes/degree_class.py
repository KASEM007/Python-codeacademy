class Fahrenheit_to_celsius:
    def __init__(self, value):
        self.temperature = value  # This calls the setter

    def temperature(self):
        return 5.0 / 9 * (self._temperature - 32)
        # In python The underscore(_) at the beginning of a variable
        # name can be used to denote a "private variable"

    def temperature(self, value):
        if value >= -459.67:
            self._temperature = value
        else:
            raise ValueError("There is no temprature below -459.67")


# main code
x = Fahrenheit_to_celsius(-50)

print(x.temperature)  # This calls the getter

x.temperature = -60  # This calls the setter
print(x.temperature)  # This calls the getter

x.temprature = -500  # This calls the setter and throws an error

print(x.temperature)  # This never executed. The flow of execution is stopped
# due to the previous statment

