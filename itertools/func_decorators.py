## https://www.youtube.com/watch?v=WOHsHaaJ8VQ

# 1. Functions are objects

##def add_five(num):
##    print(num + 5)
##
###add_five(2)
#print(add_five) # we get the location address

# 2. Function with functions

##def add_five(num):
##    def add_two(num):
##        return num + 2
##
##    num_plus_two = add_two(num)
##    print(num_plus_two + 3)
##
### add_two(7) # we get error because the add_two func
###only aviliable from inside the function
##
##add_five(10)
    
# 3. Returning functions from functions

##def get_math_function(operation): # + or -
##    def add(n1, n2):
##        return n1 + n2
##    def sub(n1, n2):
##        return n1 - n2
##
##    
##    if operation == '+':
##        return add
##    elif operation == '-':
##        return sub
##
##add_func = get_math_function('+')
###add_func = get_math_function('-')
##
##print(add_func(4, 6))


# 4. Decorating a function

##def title_decorator(print_name_function):
##    def wrapper():
##        print("Doctor: ")
##        print_name_function()
##    return wrapper
##
##
##        
##def print_my_name():
##    print("Kasem")
##    
##def print_susu():
##    print("SUSU")
##    
##decorated_function = title_decorator(print_my_name)
##decorated_function1 = title_decorator(print_susu)
##
##decorated_function()
##decorated_function1()

# 5. Decorators

##def title_decorator(print_name_function):
##    def wrapper():
##        print("Doctor: ")
##        print_name_function()
##    return wrapper
##
##
##@title_decorator       
##def print_my_name():
##    print("Kasem")
##    
##@title_decorator     
##def print_susu():
##    print("SUSU")
##    
##print_my_name()
##print_susu()

# 7. Decorators w/ Parameters

def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):
        print("Doctor: ")
        print_name_function(*args, **kwargs)
    return wrapper


@title_decorator       
def print_my_name(name, age):
    print(name + " you are " + str(age) + " years old")

print_my_name("lily", 30)
















