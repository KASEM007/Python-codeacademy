# MO’s shipping
# MO’s runs the biggest shipping company in the LA-county area,
# MO’s Shippers. Mo wants to make sure that every single one of
# his customers has the best, and most affordable experience shipping
# their packages. In this project, you’ll build a program that will
# take the weight of a package and determine the cheapest way to ship
# that package using MO’s Shippers.

# Sal’s Shippers has several different options for a customer to ship their
# package. They have ground shipping, which is a small flat charge plus a
# rate based on the weight of your package. Premium ground shipping, which
# is a much higher flat charge, but you aren’t charged for weight.
# They recently also implemented drone shipping, which has no flat charge,
# but the rate based on weight is triple the rate of ground shipping.
# Shippers has several different options for a customer to ship their package.
# They have ground shipping, which is a small flat charge plus a rate based on
# the weight of your package. Premium ground shipping, which is a much higher
# flat charge, but you aren’t charged for weight.
# They recently also implemented drone shipping, which has no flat charge,
# but the rate based on weight is triple the rate of ground shipping.

# Here are the prices:

# ****************************** Ground Shipping *******************************

# weight of package                    price per pound               Flat Charge

# 2 lb or less                              $ 1.50                     $ 20.00

# over 2 lb but <= 6lb                      $ 3.00                     $ 20.00

# over 6 lb but <= 10lb                     $ 4.00                     $ 20.00

# over 10 lb                                $ 4.75                     $ 20.00


# ****************************** Drone Shipping *******************************

# weight of package                    price per pound               Flat Charge

# 2 lb or less                              $ 4.50                     $ 00.00

# over 2 lb but <= 6lb                      $ 9.00                     $ 00.00

# over 6 lb but <= 10lb                     $ 12.00                    $ 00.00

# over 10 lb                                $ 14.25                    $ 00.00

# ****************************** Premium Ground Shipping **********************

# Flat Charge: $125

# Write a program that asks the user for the weight of their package and
# then tells them which method of shipping is cheapest and how much it will
# cost to ship their package using Mo's Shippers.


def G_shipping(weight):
    if weight <= 2:
        price_per_pound = 1.50
    elif weight <= 6:
        price_per_pound = 3.00
    elif weight <= 10:
        price_per_pound = 4.00
    else:
        price_per_pound = 4.75

    return 20 + (price_per_pound * weight)


def D_shipping(weight):
    if weight <= 2:
        price_per_pound = 4.50
    elif weight <= 6:
        price_per_pound = 9.00
    elif weight <= 10:
        price_per_pound = 12.00
    else:
        price_per_pound = 14.25

    return price_per_pound * weight


cost_of_P_G_shipping = 125.00


def best_shipping_option(weight):
    Standar = G_shipping(weight)
    Drone = D_shipping(weight)
    Premium = cost_of_P_G_shipping

    if Standar < Drone and Standar < Premium:
        method = "Standar Shipping"
        cost = Standar
    elif Drone < Standar and Drone < Premium:
        method = "Drone Shipping"
        cost = Drone
    else:
        method = "Premium Shipping"
        cost = Premium

    print(
        f"\nThe best shipping option for your package is {method}, and it will cost you only ${cost,f2.} , thank you for your bussines.\n"
    )


best_shipping_option(4.8)

best_shipping_option(41.5)
