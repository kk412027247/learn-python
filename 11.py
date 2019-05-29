s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print('%.1f %%' % r)

L = [
	['Apple', 'Google', 'Microsoft'],
	['Java', 'Python', 'Ruby', 'PHP'],
	['Adam', 'Bart', 'Lisa']
]

print(L[0][0], L[1][1], L[2][2])

age = 3

if age >= 18:
	print('your age is', age)
	print('adult')
elif age >= 6:
	print('your age is', age)
	print('teenager')
else:
	print('kid')

# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
# 	print('before 00')
# else:
# 	print('after 00')

height = 1.75
weight = 80.5
bmi = weight / (height ** 2)
if bmi < 18.5:
	print('too light')
elif 18.5 <= bmi < 25:
	print('normal')
elif 25 <= bmi < 28:
	print('overweight')
elif 28 <= bmi < 32:
	print('fat')
else:
	print('fat ass')
