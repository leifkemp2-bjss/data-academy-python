class Holding():
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    # Getters and setters
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, newprice):
        if not isinstance(newprice, float):
            raise TypeError("Expected float")
        if newprice < 0:
            raise ValueError("Must >= 0")
        self._price = newprice

    @property
    def shares(self):
        return self._shares
    
    @shares.setter
    def shares(self, newshares):
        if not isinstance(newshares, int):
            raise TypeError("Expected int")
        self._shares = newshares

    # Declaring this as a property, meaning it can be called as h.cost like a normal attribute
    @property
    def cost(self):
        return self.shares * self.price
    
    def sell(self, nshares):
        self.shares -= nshares

    def __repr__(self):
        return "{:<5s} {:<12s} {:<6d} {:<6.2f}\n".format(self.name, self.date, self.shares, self.price)

    def __str__(self):
        return "{} shares of {} at ${:0.2f}\n".format(self.shares, self.name, self.price)

import csv

class Portfolio(object):
    def __init__(self):
        self.holdings = []

    # Allows Portfolio to pick up methods
    def __getattr__(self, name):
        return getattr(self.holdings, name)

    @classmethod
    def from_csv(cls, filename):
        self = cls()
        with open(filename, 'r') as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                h = Holding(row[0], row[1], int(row[2]), float(row[3]))
                self.holdings.append(h)

        return self

    def total_cost(self):
        return sum([h.shares * h.price for h in self.holdings])

    def __len__(self):
        return len(self.holdings)
    
    def __getitem__(self, n):
        if isinstance(n, str):
            return [ h for h in self.holdings if h.name == n ]
        else:
            return self.holdings[n]
    
    def __iter__(self):
        return self.holdings.__iter__()
    
# Creates a read-only wrapper to ensure that attributes in this wrapper cannot be set
class ReadOnly():
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        return getattr(self._obj, name)
    
    def __setattr__(self, name, value):
        if name == '_obj':
            super().__setattr__(name, value)
        else:
            raise AttributeError("Read only")
    
portfolio = Portfolio.from_csv("../data/portfolio.csv")
print(portfolio)

h = Holding("Foo", "2020-10-10", 100, 10.0)

portfolio[1].price = 32.0

ro = ReadOnly(h)
# Should throw an AttributeError
ro.shares = 50