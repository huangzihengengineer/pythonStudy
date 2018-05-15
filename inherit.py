class Animal(object):
    def run(self):
        print('Animal is running......')


class Dog(Animal):
    def run(self):
        print('Dog is running.....')


a = Dog()
a.run()


# print(isinstance(a, Dog))
# print(isinstance(a,Animal))

def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())
run_twice(None)
