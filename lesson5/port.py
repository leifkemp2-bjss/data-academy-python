# Expanded on Lesson 4's port.py, but with bad data and exception handling

import csv
import glob

# using the *, as an argument enforces keyword writing style when calling function
def read_portfolio(filename, *, errors='warn'):
    '''
    Read a CSV file with name, date, shares, price data into a list.
    '''

    if errors not in { 'warn', 'silent', 'raise' }:
        raise ValueError("errors must be one of 'warn', 'silent', 'raise'")
    
    portfolio = []  # List of records
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows) # Skip the header row
        # enumerate adds an extra counter for the loop
        for rowno, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                if errors == 'warn':
                    print('Row:', rowno, 'Bad row:', row)
                    print('Row:', rowno, 'Reason:',err)
                elif errors == "raise":
                    raise
                else:
                    pass
                continue

            # record = tuple(row)
            record = {
                "name": row[0],
                "date": row[1],
                "shares": row[2],
                "price": row[3]
            }
            portfolio.append(record)

    return portfolio

portfolio = read_portfolio('../data/portfolio.csv', errors='silent')
print(portfolio)

total = 0.0

# for name, date, shares, price in portfolio: # Unpack the tuple
#     total += shares * price

for holding in portfolio:
    total += holding["shares"] * holding["price"]

print("Total cost:", total)