class InsurancePolice:
    def __init__(self, price_of_INS_item):
        self.price_of_INS_item = price_of_item


class Car_INS(InsurancePolice):
    def get_quote(self):
        return self.price_of_INS_item * .001


class Home_INS(InsurancePolice):
    def get_quote(self):
        return self.price_of_INS_item * .00005
