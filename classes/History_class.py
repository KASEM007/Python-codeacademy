class HistoryEvents:
    def __init__(self, day):
        self.day = day  # Instance field unique to each instance
        self.events = []


# main code
h1 = HistoryEvents("4th of July")
h1.events.append("1776: Declaration of independence in United State")
h1.events.append("1810: French troops occupy Amsterdam")

h2 = HistoryEvents("28th of october")
h2.events.append("969: Byzantine troops occupy Antioch")
h2.events.append("1940: ohi Day in Greece")

print(h1.events)
