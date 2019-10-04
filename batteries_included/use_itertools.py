import itertools

natuals = itertools.count(1)
# for n in natuals:
#     print(n)

ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

for c in itertools.chain('ABC', 'XYZ'):
    print(c)

for key, group in itertools.groupby('AaaBBbcCAAa', lambda ch: ch.upper()):
    print(key, list(group))


def pi(N):
    p, c = 0, 1
    for si in itertools.takewhile(lambda x: x <= 2 * N - 1, itertools.count(1, 2)):
        p, c = p + c * 4 / si, -c
    return p


print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
