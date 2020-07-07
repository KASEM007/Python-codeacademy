class OutOfStock(Exception):
    pass

class CandleShop:
    name = "Hot Candel"

    def __init__(self, stock):
        self.stock = stock

    def buy(self, color):
        if self.stock[color] < 1:
            raise OutOfStock
        else:
            self.stock[color] = self.stock[color] - 1


candel_shop = CandleShop({'Blue' : 6, 'Red':2, 'Green':0})
candel_shop.buy('Blue')
candel_shop.buy('Red')

#candel_shop.buy('Green')
print(candel_shop.stock)

print(candel_shop.name)














