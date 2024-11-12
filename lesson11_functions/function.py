import time
def after(seconds, func):
    time.sleep(seconds)
    func()

# This can be passed in as a parameter like an object
def hello():
    print('Hello world')

def add(x, y):
    def do_add():
        print(f'Adding {x} + {y} -> {x+y}')
        return x+y
    return do_add

# after(5, hello)
# First calling the outer function
a = add(2, 3)
# Then calling the inner function
a()