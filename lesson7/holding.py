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

    def __str__(self):
        return "{:<5s} {:<12s} {:<6d} {:<6.2f}\n".format(self.name, self.date, self.shares, self.price)

    def __repr__(self):
        return "{:<5s} {:<12s} {:<6d} {:<6.2f}\n".format(self.name, self.date, self.shares, self.price)

import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            h = Holding(row[0], row[1], int(row[2]), float(row[3]))
            portfolio.append(h)

        return portfolio
    
portfolio = read_portfolio("../data/portfolio.csv")
print(portfolio)

import table

table.print_table(portfolio, ['name', 'shares'])