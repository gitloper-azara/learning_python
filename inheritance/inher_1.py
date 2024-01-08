#!/usr/bin/python3

# a python program to demonstrate inheritance
class Person(object):

    # constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # to check if this person is an employee
    def Display(self):
        print(self.name, self.id)


# driver code
emp = Person("Saytam", 102) # an object of Person
emp.Display()


class Emp(Person):

    def Print(self):
        print('Emp class called')

Emp_details = Emp('Mayank', 103)

# calling parent class function
Emp_details.Display()

# calling child class function
Emp_details.Print()
