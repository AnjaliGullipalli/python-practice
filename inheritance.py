class animal:
    def __init__(self,age,name):
        self.name=name
        self.age=age
    def sound(self):
        print('i can make loud sound')
    def eat(self):
        print('i can eat')
class Dog(animal):
    def display(self):
        print('my name is',self.age)
        print('my age is ',self.name)
d1=Dog('bunny',18)
d1.eat()
d1.sound()
d1.display()


