from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

# from collections import ChainMap
#
# import os, argparse

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
dd = defaultdict(lambda: 'N/A')

dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)

od = OrderedDict(d)
print(od)

od = OrderedDict()

od['z'] = 1
od['y'] = 2
od['x'] = 3
print(od.keys())

#
# class LastUpdateOrderDict(OrderedDict):
#     def __init__(self, capacity):
#         super(LastUpdateOrderDict, self).__init__()
#         self._capacity = capacity
#
#

c = Counter()

for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
