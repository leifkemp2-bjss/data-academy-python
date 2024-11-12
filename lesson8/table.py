import sys
from abc import ABC, abstractmethod # implements abstract classes

class TableFormatter(ABC):
    def __init__(self, outfile=None):
        if outfile == None:
            outfile = sys.stdout
        self.outfile = outfile

    # A design spec for making tables (use inheritance to customize)
    @abstractmethod
    def headings(self, headers):
        pass
    
    @abstractmethod
    def row(self, rowdata):
        pass    
class TextTableFormatter(TableFormatter):
    def __init__(self, outfile=None, width = 10):
        super().__init__(outfile) # Initialize parent
        self.width = width

    def headings(self, headers):
        for header in headers:
            print("{:>{}s}".format(header, self.width), end = ' ')
        print()

    def row(self, rowdata):
        for item in rowdata:
            print("{:>{}s}".format(item, self.width), end = ' ')
        print()

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end='')
        for header in headers:
            print("<th>{}</th>".format(header), end = ' ')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for row in rowdata:
            print("<th>{}</th>".format(row), end = ' ')
        print('</tr>')

def print_table(objects, colnames, formatter):
    if not isinstance(formatter, TableFormatter): # Prevents passing bad inputs
        raise TypeError('formatter must be a TableFormatter')
    formatter.headings(colnames)
    for obj in objects:
        rowdata = [str(getattr(obj, colname)) for colname in colnames]
        formatter.row(rowdata)