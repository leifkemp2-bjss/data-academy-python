import table

# This object expands on TextTableFormatter, but only inherits from that class so its use is limited
class QuotedTextTableFormatter(table.TextTableFormatter):
    def row(self, rowdata):
        # Puts quotes around all values
        quoted = [ '"{}"'.format(d) for d in rowdata ]
        super().row(quoted)

# An example of multiple inheritance
class QuotedMixin(object):
    def row(self, rowdata):
        # Puts quotes around all values
        quoted = [ '"{}"'.format(d) for d in rowdata ]
        super().row(quoted)

class Formatter(QuotedMixin, table.CSVTableFormatter):
    pass