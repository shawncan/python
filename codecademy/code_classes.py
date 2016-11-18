#!/usr/local/bin/Python3"default_encoding": "UTF-8",
# -*- coding: utf-8 -*-


class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        return "This is a %s %s with %s MPG." % (self.color, self.model, self.mpg)

    def drive_car(self):
        self.condition = "used"


class ElectricCar(Car):

    def __init__(self, battery_type, model, color, mpg):
        self.battery_type = battery_type
        self.model = model
        self.color = color
        self.mpg = mpg

    def drive_car(self):
        self.condition = "like new"


class Point3D(object):
    """11有用的函数"""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)


my_car = Car("DeLorean", "silver", 88)
print(my_car.condition)
print(my_car.model)
print(my_car.color)
print(my_car.mpg)
print(my_car.condition)
print(my_car.drive_car())
print(my_car.condition)
my_car1 = ElectricCar("molten salt", "DeLorean", "silver", 88)
print(my_car1.condition)
print(my_car1.drive_car())
print(my_car1.condition)
my_point = Point3D(1, 2, 3)
print(my_point)