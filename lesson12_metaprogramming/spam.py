import logcall

@logcall.logmethods
class Spam():
    def __init__(self, value):
        self.value = value

    def yow(self):
        print("YOW!")

    def grok(self):
        print("Grok!")

s = Spam(5)
s.yow()