#!/usr/bin/python3
class Person:
    def __init__(self, name) -> None:
        self.name = name


    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Azara')
p.say_hi()
# or
Person('Azara').say_hi()
