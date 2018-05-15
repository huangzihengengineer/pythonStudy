class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sex = '帅哥'
        self.__height=175

    def print(self):
        print('%s %s' % (self.name, self.sex))

    def _print(self):
        print('private method')


s = Student('hzh', '18')

s.print()
print(s._Student__height)
print(__file__)