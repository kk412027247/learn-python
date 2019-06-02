import math

n1 = 255
n2 = 1000
print(str(hex(n1)), str(hex(n2)))


def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x


print(my_abs(-1))


# print(my_abs('a'))


def nop():
	pass


def move(x, y, step, angle=0.0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r)


def quadratic(a, b, c):
	x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
	x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
	return x1, x2


x1, x2 = quadratic(1, 20, 3)
print(x1, x2)

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
	print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
	print('测试失败')
else:
	print('测试成功')


def power(x, n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s


print(power(5, 2))
print(power(5, 3))
print(power(5))


def enroll(name, gender, age=6, city='Beijing'):
	print('name: ', name)
	print('gender: ', gender)
	print('age: ', age)
	print('city: ', city)


enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')


def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L


print(add_end())
print(add_end())


def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum


print(calc([1, 2, 3]))
print(calc((1, 3, 5, 7)))


def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum


print(calc(1, 3, 5, 7))

print(calc(*(1, 3, 5, 7)))


def persion(name, age, **kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print('name:', name, 'age: ', age, 'other: ', kw)


print(persion('Michael', 30))
print(persion('Bob', 35, city='Beijing'))
print(persion('Adam', 45, gender='M', job='Engineer'))

extra = {'city': 'Beijing', 'job': 'Engineer'}
print(persion('Jack', 24, **extra))


def persion(name, age, *, city, job):
	print(name, age, city, job)


print(persion('Jack', 24, city='Beijing', job='Enginner'))


def persion(name, age, *args, city, job):
	print(name, age, args, city, job)


print(persion('Jack', 24, 1, 2, 3, city='Beijing', job='Enginner'))


def persion(name, age, *, city='Beijing', job):
	print(name, age, city, job)


print(persion('Jack', 24, job='Enginner'))


def f1(a, b, c=0, *args, **kw):
	print(a, b, c, args, kw)


def f2(a, b, c=0, *, d, **kw):
	print(a, b, c, d, kw)


print(f1(1, 2))
print(f1(1, 2, c=3))
print(f1(1, 2, 3, 'a', 'b'))
print(f1(1, 2, 3, 'a', 'b', x=99))
print(f2(1, 2, d=99, ext=None))

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
print(f1(*args, **kw))
print(f2(*(1, 2, 3), **kw))


def product(*numbers):
	result = 1
	if len(numbers) == 0:
		raise TypeError
	for number in numbers:
		result = number * result
	return result


print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))

if product(5) != 5:
	print('测试失败!')
elif product(5, 6) != 30:
	print('测试失败!')
elif product(5, 6, 7) != 210:
	print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
	print('测试失败!')
else:
	try:
		product()
		print('测试失败!')
	except TypeError:
		print('测试成功!')


def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)


print(fact(1))
print(fact(5))


# print(fact(1000))

def fact(n):
	return fact_inter(n, 1)


def fact_inter(num, product):
	if num == 1:
		return product
	return fact_inter(num - 1, num * product)

# print(fact(1000))
