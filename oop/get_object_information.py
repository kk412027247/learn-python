import types

print(type(123))

print(type('str'))

print(type(None))

print(type(abs))


def fn():
    pass


print(type(fn) == types.FunctionType)

print(isinstance([1, 2, 3], (list, tuple)))

print(dir('ABC'))


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

print(hasattr(obj, 'x'))

print(hasattr(obj, 'y'))

setattr(obj, 'y', 19)

print(hasattr(obj, 'y'))

print(getattr(obj, 'y'))
