# Adds a welcome message to the string
# returned by fun(). Takes fun() as
# parameter and returns welcome().
def decorate_message(fun):
 
    # Nested function
    def addWelcome(site_nam):
        return "Welcome to " + fun(site_nam)
 
    # Decorator returns a function
    return addWelcome
 
@decorate_message
def site(site_name):
    return site_name;
 
# Driver code
 
# This call is equivalent to call to
# decorate_message() with function
# site("GeeksforGeeks") as parameter
print site("GeeksforGeeks")

"""def decorator(f):
   #process function
   return f
it automatically maps the following:

@decorator
def f(arg):
   return arg*arg

f(123)  # output 15129"""
