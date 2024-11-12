def __init__(self, x, y):
    self.x = x
    self.y = y

def move(self, dx, dy):
    self.x += dx
    self.y += dy

name = "point"
bases = (object,)
methods = {
    "__init__": __init__,
    "move": move
}

# creating a metaclass allows intercepting the type method to customise creation of types
class mytype(type):
    def __new__(meta, clsname, bases, methods):
        print('Creating:', clsname)
        print('Bases:', bases)
        print('Methods:',list(methods))
        return super().__new__(meta, clsname, bases, methods)
    
class Point(metaclass=mytype):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def foo(self):
        print("FOO")

p = Point(2, 3)
p.move(1, 1)
p.foo()

print(f"{p.x},{p.y}")