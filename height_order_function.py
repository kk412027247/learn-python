from functools import reduce


def add(x, y, f):
    return f(x) + f(y)


x = -5
y = 6

print(add(x, y, abs))


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))


def fn(x, y):
    return x * 10 + y


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': -1}


def char2num(s):
    return DIGITS[s]


print(reduce(fn, map(char2num, '13579')))


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int('13579'))


def lower(s):
    return s.lower().capitalize()


L1 = ['adam', 'LISA', 'barT']


def normalize(name):
    return list(map(lower, name))


print(normalize(L1))


def prod(L):
    return reduce(lambda x, y: x * y, L)


print(prod([3, 5, 7, 9]))


def str2float(s):
    nums = map(lambda ch: DIGITS[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        print('point',point)
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point

    return reduce(to_float, nums, 0.0)

print(str2float('123.456'))
