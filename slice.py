L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[-1:])
print(L[-2:])
print(L[-2: -1])

L = list(range(100))
print(L[:10])
print(L[-10:])
print(L[10:20])

print(L[:10:2])
print(L[::5])
print(L[:])

print((0, 1, 2, 3, 4)[:3])

print('ABCDEFG'[:3])
print('ABCDEFG'[::2])


def trim(s):
	if s == '' or (s[0] != ' ' and s[-1] != ' '):
		return s
	elif s[0] == ' ':
		return trim(s[1:])
	else:
		return trim(s[:-1])


# 测试:
if trim('hello  ') != 'hello':
	print('测试失败!')
elif trim('  hello') != 'hello':
	print('测试失败!')
elif trim('  hello  ') != 'hello':
	print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
	print('测试失败!')
elif trim('') != '':
	print('测试失败!')
elif trim('    ') != '':
	print('测试失败!')
else:
	print('测试成功!')
