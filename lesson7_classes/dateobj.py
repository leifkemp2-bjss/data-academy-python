class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, s):
        parts = s.split('-')
        return cls(int(parts[0]), int(parts[1]), int(parts[2]))
    
    @classmethod
    def today(cls):
        import time
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)
    
class DateThatScreamsAtYou(Date): # Inherits from Date
    def scream(self):
        print("AAAAAAAAAAAAAAAAAAAAAAA")
    
date1 = Date(2024, 11, 11)
date2 = Date.from_string("2024-11-11")
date3 = Date.today()
date4 = DateThatScreamsAtYou.today()
date4.scream()