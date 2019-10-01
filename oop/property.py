class Student(object):
    def __init__(self, name):
        self.name = name


s = Student('Bob')
s.score = 90


class Student(object):
    name = 'Student'


s = Student()

print(s.name)

s.name = 'Michael'

print(s.name)

del s.name

print(s.name)


class Student(object):
    count = 0

    def __init__(self, name):
        Student.count = self.count + 1
        self.name = name


if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('1测试失败!' + str(Student.count))
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('2测试失败!')
        else:
            print('Students:', Student.count)
            print('3测试通过!')
