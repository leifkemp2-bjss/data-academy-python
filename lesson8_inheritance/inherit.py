class Parent():
    def __init__(self, value):
        self.value = value

    def spam(self):
        print("Parent.spam", self.value)

    def grok(self):
        print("Parent.grok")
        self.spam()

class Parent2():
    def scream(self):
        print("OWWWWWWWWWWWWWWWW")

class Child(Parent):
    def __init__(self, value, extra):
        self.extra = extra
        super().__init__(value) # Initialize parent

    def yow(self):
        print("Child.yow")

    def spam(self):
        print("Child.spam", self.value)

class Child2(Parent):
    def spam(self):
        print("Child2.spam")
        super().spam() # Invokes original spam

class Child3(Parent, Parent2):
    pass

c = Child(42, 1)
c.spam()
c.yow()
c.grok()

c2 = Child2(24)
c2.spam()

c3 = Child3(32)
c3.scream()
c3.spam()