def print_square(func):
    def wrapper(num):
        return func(num)**2
    return wrapper

@print_square
def get_number(num):
    return num

print get_number(2)
    
