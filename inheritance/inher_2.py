#!/usr/bin/python3
# a python program to demosntrate inheritance

# base or super class. note object in bracket.
# (generally, object is made ancestor of all classes)
# in python 3.x 'class Person' is
# equivalent to 'class Person(object)'


class Person(): # can as well write as 'class Person(object)'

    # constructor
    def __init__(self, name) -> None:
        self.name = name

    # to get name
    def getName(self):
        return self.name
    
    def isEmployee(self):
        return False
    

# inherited or subclass (note person in bracket)
class Employee(Person):

    # here we return true
    def isEmployee(self):
        return True
    
# driver code
emp = Person('Geek1') # an object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee('Geek2') # an object of Employee
print(emp.getName(), emp.isEmployee())
