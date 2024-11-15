import csv

total = 0.0

with open('../data/portfolio.csv', 'r') as f:
    rows = csv.reader(f)
    headers = next(rows) # Skip the header row
    for row in rows:
        print(row)
        row[2] = int(row[2])
        row[3] = float(row[3])
        total += row[2] * row[3]

print('Total cost: %.2f' % total)