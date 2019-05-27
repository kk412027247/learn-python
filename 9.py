counter = 100
miles = 1000.0
name = 'runoob'

print(counter)
print(miles)
print(name)

a, b, c = 1, 2, "runnoob"
print(a, b, c)
a = b = c = 1
print(a, b, c)

a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))
print(isinstance(a, int))

var1 = 1
var2 = 10
print(var1, var2)
del var1, var2
# print(var1, var2)  NameError: name 'var1' is not defined

print(2 // 4, 2 // 3, 3 // 3)

str = 'Runoob'
print(str)
print(str[0: -1])
print(str[0])
print(str[2:])
print(str[2:5])
print(str * 2)
print(str + "TEST")

print('Ru\noob')
print(r'Ru\noob')

t = ['a', 'b', 'c', 'd', 'e']
print(t[1:3], t[3:], t[:4], t[:])

