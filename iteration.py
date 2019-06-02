from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print(key)

for value in d.values():
	print(value)

for ch in 'ABC':
	print(ch)

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3, 4], Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['a', 'b', 'c']):
	print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
	print(x, y)


def findMinAndMax(L):
	if len(L) == 0:
		return None, None
	min = L[0]
	max = L[0]
	if len(L) == 1:
		return min, max
	for num in L:
		if min > num:
			min = num
		if max < num:
			max = num
	return (min, max)


# 测试
if findMinAndMax([]) != (None, None):
	print('1测试失败!')
elif findMinAndMax([7]) != (7, 7):
	print('2测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
	print('3测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
	print('4测试失败!')
else:
	print('测试成功!')
