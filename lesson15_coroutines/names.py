import asyncio

async def greeting(name):
    return "Hello " + name

async def hello():
    names = ['Guido','Dave','Paula']
    for name in names:
        print(await greeting(name))

h = hello()

loop = asyncio.get_event_loop()
loop.run_until_complete(h)