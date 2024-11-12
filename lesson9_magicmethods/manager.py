# this class contains the two methods utilised in with statements
class Manager():
    def __enter__(self):
        print('Entering')
        return 'some value'
    
    def __exit__(self, ty, val, tb):
        print('Exiting')
        print(ty, val, tb) # Prints exception

m = Manager()

with m as val:
    print('Hello World')
    print(val) # returns the value provided by __enter__ method