class Typed():
    expected_type = object

    def __init__(self, name=None):
        self.name = name

    # Descriptor
    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f'Expected {self.expected_type}')
        instance.__dict__[self.name] = value

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str

class Holding():
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price
    
    @property
    def cost(self):
        return self.shares * self.price
    
h = Holding('Foo', '2020-10-10', 12, 12.0)
print(h.cost)

# Should raise a TypeError as shares should have int enforced as a type
h2 = Holding('Foo', '2020-10-10', '12', 12.0)