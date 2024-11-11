from . import reader # Package-relative import
# import portie.reader

def read_portfolio(filename, *, errors='warn'):
    return reader.read_csv(filename, [str, str, int, float], errors=errors)

# silences the code unless it is the main program
if __name__ == '__main__':
    records = read_portfolio("../data/portfolio.csv", [str,str,int,float])
    print(records)