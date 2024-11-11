# Expanded on Lesson 4's port.py, but with bad data and exception handling

import csv
import glob

# using the *, as an argument enforces keyword writing style when calling function
def portfolio_cost(filename, *, errors='warn'):
    '''
    Computes total shares*price for a CSV file with name, date, shares, price data
    '''

    if errors not in { 'warn', 'silent', 'raise' }:
        raise ValueError("errors must be one of 'warn', 'silent', 'raise'")
    
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
                if errors == 'warn':
                    print('Row:', rowno, 'Bad row:', row)
                    print('Row:', rowno, 'Reason:',err)
                elif errors == "raise":
                    raise
                else:
                    pass

                continue
        
        total += row[2] * row[3]

    return total

# glob will grab all files with matching pattern
# files = glob.glob('../data/portfolio*.csv')
# print(files)

# for file in files:
#     total = portfolio_cost(file)
#     print('Total cost: %.2f' % total)

total = portfolio_cost('../data/missing.csv', errors='silent')
print(total)