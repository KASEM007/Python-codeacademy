class Tesla:
    Type = "Electric"
    Roof = "Glass"

    def __init__(self, model, doors, seats, Type):
        self.model = model
        self.doors = doors
        self.number_of_seats = seats
        self.type_of_car = Type

    def car_info(self):
        return f"{self.model} - {self.Type} - {self.type_of_car} - {self.doors}"


tesla_s = Tesla("Model(S)", "4D", "5 seats", "Sedan")
tesla_y = Tesla("Model(Y)", "4D", "5 seats", "Sedan")
tesla_x = Tesla("Model(X)", "5D", "7 seats", "SUV")

# print(
#     tesla_s.model,
#     tesla_s.type_of_car,
#     tesla_s.number_of_seats,
#     tesla_s.Type,
#     tesla_s.Roof,
# )

print(tesla_s.car_info())
