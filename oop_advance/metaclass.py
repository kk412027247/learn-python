class Hello(object):
    def hello(self, name='world'):
        print('hello, %s.' % name)


h = Hello()

h.hello()

print(type(Hello), type(h))


def fn(self, name='world'):
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()

h.hello()


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()

L.add(1)

print(L)

# L2 = list()
# L2.add(1)
