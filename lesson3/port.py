# f = open('data/portfolio.csv', 'r')
# for line in f:
#     print(line)

total = 0.0

# using with open automatically closes the file when finished
with open('../data/portfolio.csv', 'r') as f:
    headers = next(f) # Skips a line
    for line in f:
        line = line.strip()
        parts = line.split(',')
        parts[0] = parts[0].strip('"')
        parts[1] = parts[1].strip('"')
        parts[2] = int(parts[2])
        parts[3] = float(parts[3])
        print(parts)
        total += parts[2] * parts[3]

print('Total cost: %.2f' % total)