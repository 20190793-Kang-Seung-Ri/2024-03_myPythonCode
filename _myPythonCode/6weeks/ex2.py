# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:34:34 2024

@author: irunn
"""

import turtle
import random

turtleList = [ ]
colorList = ["red", "green", "blue", "black", "magenta", "orange", "gray"]
shapeList = ["arrow", "circle", "square", "triangle", "turtle"]

turtle.setup(550, 550)
turtle.screensize(500, 500)

for i in range(100): # 거북이 100마리 생성
    shape = random.choice(shapeList)
    color = random.choice(colorList)
    
    x = random.randint(-250, 250) # 거북이가 이동할 좌표값
    y = random.randint(-250, 250)
    
    Tshape = turtle.Turtle(shape)
    
    tup = (Tshape, color, x, y) # 튜플 생성
    turtleList.append(tup) # 튜플을 리스트에 추가

for i in turtleList: # 리스트에 담긴 거북이 100마리 그리기
    Tshape = i[0]
    Tshape.pencolor(i[1])
    Tshape.goto(i[2], i[3])

turtle.done()
