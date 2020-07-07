# Exception that gets thrown when a kitchen appliance isn't working
class KitchenException(Exception):
    pass

# Exception for when the microwave stops working
class MicrowaveException(KitchenException):
    pass

# Exception for when the refrigerator stops working
class RefrigeratorException(KitchenException):
    pass

## In this code, we define three exceptions.
## First, we define a KitchenException that acts as
## the parent to our other, specific kitchen appliance exceptions.
## KitchenException subclasses Exception, so it behaves in the same
## way that regular Exceptions do. Afterward we define
## MicrowaveException and RefrigeratorException as subclasses.
## Since our exceptions are subclassed in this way,
## we can catch any of KitchenException‘s subclasses by catching
## KitchenException.
## For example:

def get_food_from_fridge():
    if refrigerator.cooling == False:
        raise RefrigeratorException
    else:
        return food

def heat_food(food):
    if microwave.working == False:
        raise MicrowaveException
    else:
        microwave.cook(food)
        return food

try:
    food = get_food_from_fridge()
    food = heat_food(food)
except KitchenException:
    food = order_takeout()

## In the above example, we attempt to retrieve food from the fridge
## and heat it in the microwave. If either RefrigeratorException or
## MicrowaveException is raised, we opt to order takeout instead.
## We catch both RefrigeratorException and MicrowaveException in
## our try/except block because both are subclasses of KitchenException.





    
