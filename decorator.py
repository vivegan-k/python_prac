def square(func):
    def wrapper(num):
        return func(num) ** 2
    return wrapper

@square
def get_number(num):
    return num

print(get_number(2))


def sum_n(func):
    def wrapper(*args):
        sum1 = 0
        for arg in args:
            sum1 += arg
        return sum1
    return wrapper

@sum_n
def get_numbers(*args):
    return args

print(get_numbers(1,2,3,4))