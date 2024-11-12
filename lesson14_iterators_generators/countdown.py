def countdown(n): # This creates a generator function
    print("Counting down from",n)
    while n > 0:
        yield n # Emits a value and suspends the while loop until __next__() is called on it
        n -= 1
    print("Done")

for x in countdown(5):
    print(x)

c = countdown(5)
it = c.__iter__()
print(it.__next__()) # Can be called repeatedly, will stop when it hits a StopIteration exception