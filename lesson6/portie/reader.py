# Expanded on Lesson 4's port.py, but as a general purpose library

import csv

# using the *, as an argument enforces keyword writing style when calling function
def read_csv(filename, types, *, errors='warn'):
    '''
    Read a CSV file with type conversion into a list of dicts
    '''

    if errors not in { 'warn', 'silent', 'raise' }:
        raise ValueError("errors must be one of 'warn', 'silent', 'raise'")
    
    records = []  # List of records
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows) # Skip the header row
        # enumerate adds an extra counter for the loop
        for rowno, row in enumerate(rows, start=1):
            try:
                row = { func(val) for func, val in zip(types, row) }
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
            record = dict(zip(headers, row))
            records.append(record)

    return records