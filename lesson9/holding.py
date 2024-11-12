class Holding():
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

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
        print("AA???")
        if isinstance(n, str):
            return [ h for h in self.holdings if h.name == n ]
        else:
            print("Returning this")
            return self.holdings[n]
    
    def __iter__(self):
        return self.holdings.__iter__()
    
portfolio = Portfolio.from_csv("../data/portfolio.csv")
print(portfolio)

print(len(portfolio))
print(portfolio[2])
print(portfolio.__getitem__(2))
print(portfolio["MSFT"])
# table.print_table(portfolio, ['name', 'shares'])