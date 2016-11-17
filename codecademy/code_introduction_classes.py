#!/usr/local/bin/Python3"default_encoding": "UTF-8",
# -*- coding: utf-8 -*-


class ShoppingCart(object):
    """Creates shopping cart objects for users of our fine website."""
    items_in_cart = {}

    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print(product + "添加成功。")
        else:
            print(product + "已存在购物车中。")

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print(product + "删除成功。")
        else:
            print(product + "不在购物车中。")

    def sum_item(self):
        item_costs = 0
        for i in self.items_in_cart.values():
            item_costs += i
        print(item_costs)


class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name, hours):
        self.employee_name = employee_name
        self.hours = hours

    def calculate_wage(self):
        return self.hours * 20.00


# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self,):
        return self.hours * 12.00

    def full_time_wage(self):
        return super(PartTimeEmployee, self).calculate_wage()


class Triangle(object):
    """ 三角形类 """
    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False


class Equilateral(Triangle):
    angle = 60

    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle


my_cart = ShoppingCart("wjc")
my_cart.add_item("苹果", 28)
my_cart.add_item("梨", 30)
my_cart.add_item("火龙果", 50)
my_cart.remove_item("苹果")
my_cart.sum_item()

milton = PartTimeEmployee("wangjiacan", 10)
print(milton.full_time_wage())

my_triangle = Triangle(90, 30, 60)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())

