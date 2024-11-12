def func(x, **kwargs):
    print(x)
    # takes any other keyword arguments after the first one and packages them into a dict
    print(kwargs)

# accepts any combination of positional and keyword arguments
def func2(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, xmin=10, xmax=20, color='red')
func2(1, 2, x=3,y=4)