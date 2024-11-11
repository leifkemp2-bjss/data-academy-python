# Expanded on Lesson 4's port.py, but with bad data and exception handling

import csv
import glob

def portfolio_cost(filename):
    '''
    Computes total shares*price for a CSV file with name, date, shares, price data
    '''
    total = 0.0

    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows) # Skip the header row
        # enumerate adds an extra counter for the loop
        for rowno, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                print('Row:', rowno, 'Bad row:', row)
                print('Row:', rowno, 'Reason:',err)
                continue
        
        total += row[2] * row[3]

    return total

# glob will grab all files with matching pattern
# files = glob.glob('../data/portfolio*.csv')
# print(files)

# for file in files:
#     total = portfolio_cost(file)
#     print('Total cost: %.2f' % total)

total = portfolio_cost('../data/missing.csv')
print(total)