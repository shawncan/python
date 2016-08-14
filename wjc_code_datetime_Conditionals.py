#!/usr/local/bin/Python3"default_encoding": "UTF-8",
# -*- coding: utf-8 -*-

#20160811
# def clinic():
#     print("You've just entered the clinic!")
#     print("Do you take the door on the left or the right?")
#     answer = input("Type left or right and hit 'Enter'.").lower()
#     if answer == "left" or answer == "l":
#         print("This is the Verbal Abuse Room, you heap of parrot droppings!")
#     elif answer == "right" or answer == "r":
#         print("Of course this is the Argument Room, I've told you that already!")
#     else:
#         print("You didn't pick left or right! Try again.")
#         clinic()

# n = clinic()


#20160814-条件控制表达式
answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return "wjc"        # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return "xxx"        # Make sure this returns False
    
n = black_knight()
b = french_soldier()

print(n)
print(b)