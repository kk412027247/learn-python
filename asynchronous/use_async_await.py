import asyncio


@asyncio.coroutine
def hello():
    print('Hello world!')
    r = yield from asyncio.sleep(1)
    print('Hello again! ')


hello()


async def hello():
    print('Hello world!')
    r = await asyncio.sleep(1)
    print('Hello again!')


hello()
