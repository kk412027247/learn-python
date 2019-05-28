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

list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)

a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [12, 14, 15]
print(a)
a[2:5] = []
print(a)

letters = ['c', 'h', 'e', 'c', 'k', 'i', 'o']
print(letters[1:4:2])


def reverseWords(input):
    inputWords = input.split(" ")
    inputWords = inputWords[-1::-1]
    output = ' '.join(inputWords)
    return output


if __name__ == '__main__':
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)

tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple * 2)
print(tuple + tinytuple)

tup1 = ()
tup2 = (20,)

print(tup1, tup2)

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)

if 'Rose' in student:
    print('Rose is in the set')
else:
    print("Rose is not in the set")

a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

dict2 = {}

dict2['one'] = '1 - guide'
dict2[2] = '2 - guide'

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict2['one'])
print(dict2[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

# print(dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)]))
dict1 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(dict1)

dict3 = {x: x ** 2 for x in (2, 3, 6)}
print(dict3)

dict4 = {'Runoob': 1, 'Google': 2, 'Taobal': 3}
print(dict4)
