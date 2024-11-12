# Watches a log file in real time
# For this code to work, you must run data/stocksim.py to update the stocklog.csv file in real time


import os
import time

def follow(filename):
    f = open(filename, 'r')
    f.seek(0, os.SEEK_END)

    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue # Retry
        yield line # Emit a line
        

# f = open('../data/stocklog.csv')
# lines = f.readlines()

for line in follow('../data/stocklog.csv'):
    row = line.split(',')
    change = float(row[4])
    if change < 0:
        name = row[0]
        price = row[1]
        print("{:>10s} {:>10s} {:>10.2f}".format(name, price, change))