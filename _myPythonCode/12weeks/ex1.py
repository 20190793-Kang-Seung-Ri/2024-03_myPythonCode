# -*- coding: utf-8 -*-
"""
Created on Mon May 20 09:38:01 2024

@author: irunn
"""

class Rabbit:
    shape = ""
    xPos = 0
    yPos = 0
    
    def goto(self, x, y):
        self.xPos = x
        self.yPos = y
        
rabbit1 = Rabbit()
rabbit2 = Rabbit()
rabbit3 = Rabbit()

rabbit1.shape = "원"
rabbit1.goto(100, 100)

rabbit2.shape = "삼각형"
rabbit2.goto(-100, 100)

rabbit3.shape = "토끼"
rabbit3.goto(0, -100)

print(f"토끼1 객체의 모양 : {rabbit1.shape}")
print(f"토끼1의 위치 : ({rabbit1.xPos}, {rabbit1.yPos})")

print(f"토끼2 객체의 모양 : {rabbit2.shape}")
print(f"토끼2의 위치 : ({rabbit2.xPos}, {rabbit2.yPos})")

print(f"토끼3 객체의 모양 : {rabbit3.shape}")
print(f"토끼3의 위치 : ({rabbit3.xPos}, {rabbit3.yPos})")