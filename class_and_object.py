class Student(object):
    pass


bart = Student()

print(bart)
print(Student)

bart.name = 'Bart Simpson'
print(bart.name)


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(std):
        print('%s: %s' % (std.name, std.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 59)
print(bart.name)
print(bart.score)


def print_score(std):
    print('%s: %s' % (std.name, std.score))


print_score(bart)

bart.print_score()

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())
