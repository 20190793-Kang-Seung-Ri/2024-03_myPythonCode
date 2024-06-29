# -*- coding: utf-8 -*-
"""
Created on Mon May 20 10:32:39 2024

@author: irunn
"""

class Car:
    color = ""
    speed = 0
    
    def __init__(self, value1, value2):
        self.color = value1
        self.speed = value2
    
    def upSpeed(self, value):
        self.speed += value
        
    def downSpeed(self, value):
        self.speed -= value

myCar1 = Car("Red", 0)
myCar2 = Car("Green", 60)
myCar3 = Car("Blue", 20)

myCar1.upSpeed(60)
print(f"자동차1의 색상 : {myCar1.color}, 현재 속도는 : {myCar1.speed}Km/h")

myCar2.upSpeed(80)
myCar2.downSpeed(50)
print(f"자동차2의 색상 : {myCar2.color}, 현재 속도는 : {myCar2.speed}Km/h")

myCar3.upSpeed(140)
myCar3.upSpeed(20)
print(f"자동차3의 색상 : {myCar3.color}, 현재 속도는 : {myCar3.speed}Km/h")