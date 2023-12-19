#!/usr/bin/python3
class Robot:
    """Represents a Robot with attributes"""

    def __init__(self, name, build_year, brand):
        """Initialises the Robot data"""
        self.name = name
        self.build_year = build_year
        self.brand = brand

x = Robot('Marvin', '1979', 'Kuka')
y = Robot('Caliban', '1993', 'Tayata')
print(x.name)
print(y.build_year)
print(x.__dict__)
print(y.__dict__)
print(x.brand)
