# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:32:16 2024

@author: irunn
"""

import turtle
import random

class Rabbit:
    myTurtle = ""
    
    def __init__(self, value):
        self.myTurtle = value
        
    def print_my_position(self):
        print(f"토끼의 위치 : ({self.myTurtle.xcor()}, {self.myTurtle.ycor()})")
        
colorList = ["red", "green", "blue", "black", "magenta", "orange", "gray"]
shapeList = ["turtle", "triangle", "circle", "square", "arrow"]

turtle.setup(550, 550)
turtle.screensize(500, 500)

myTurt = turtle.Turtle("turtle")
rabbit = Rabbit(myTurt)
myTurt.pensize(5)

for _ in range(20):
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    
    color = random.choice(colorList)
    
    myTurt.pencolor(color)
    myTurt.goto(x, y)
    
    rabbit.print_my_position()
    