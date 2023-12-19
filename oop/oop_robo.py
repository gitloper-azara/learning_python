#!/usr/bin/python3
class Robot:
    """Represents a Robot with attributes"""

    def __init__(self, name, build_year, brand):
        """Initialises the Robot data"""
        self.name = name
        self.build_year = build_year
        self.brand = brand


    def hi(self):
        """Robotic greetings and introduction"""
        if self.name:
            print('Hi, I am {}!'.format(self.name))
        else:
            print('I am a robot without a name')
    

    def set_name(self, name):
        """setter method for modifying the value of name"""
        self.name = name


    def get_name(self):
        """getter method for retriving the value of the name
        attribute"""
        return self.name

x = Robot(None,'1979', 'Kuka')
y = Robot('Caliban', '1993', 'Tayata')
x.hi()
y.hi()
print(x.name)
print(y.build_year)
print(x.__dict__)
print(y.__dict__)
print(x.brand)
x.set_name('Azara')
x.hi()
print(x.get_name())
print(x.__dict__)
