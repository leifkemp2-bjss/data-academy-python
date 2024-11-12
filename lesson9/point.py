class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other): # Magic method, implementation of python methods
        print('Add', other)