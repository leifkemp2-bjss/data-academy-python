from functools import wraps

# Wraps the logger in a new function, that allows custom logging messages
def logformat(fmt):
    def logged(func):
        # Give in a function, and put logging around it
        # Wrapping the function into a logger reduces the amount of times logging is called
        # Allowing for rewrites in only one place
        @wraps(func) # copies metadata into the wrapped func
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        
        return wrapper

    return logged

@logformat('CALLING {func.__name__}') #this is the same as doing add = logged(add)
def add(x, y):
    return x + y

@logformat('CALLING {func.__name__}')
def sub(x, y):
    return x - y

@logformat('CALLING {func.__name__}')
def mul(x, y):
    return x * y

print(add(2, 3))

logged = logformat("You called {func.__name__}")

def logmethods(cls):
    for key, value in list(vars(cls).items()):
        if callable(value):
            # Is it a method? If so, decorate
            setattr(cls, key, logged(value))
    return cls