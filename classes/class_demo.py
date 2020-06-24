class Staff:
    def __init__(self, pPosition, pName, pPay):
        self._position = pPosition
        self.name = pName
        self.pay = pPay
        print("Creating Staff object")

    def __str__(self):
        return "Position = %s, Name = %s, Pay = %d" % (
            self._position,
            self.name,
            self.pay,
        )

    def calculatePay(self):
        prompt = "\Enter number of hourse worked for %s: " % (self.name)
        hours = input(prompt)
        prompt = "Enter the hourly rate for %s: " % (self.name)
        hourlyRate = input(prompt)
        self.pay = int(hours) * int(hourlyRate)
        return self.pay

    # A decorator
    @property
    def position(self):
        print("Getter Method")
        return self._position

    # A decorator
    @position.setter
    def position(self, value):
        if value == "Manager" or value == "Basic":
            self._position = value
        else:
            print("Position is invalid. No change made")


offcieStaff1 = Staff("Basic", "Yvonne", 0)

print(offcieStaff1.name)
# offcieStaff1.position = "Manager"

print(offcieStaff1.position)

print(offcieStaff1.calculatePay())
