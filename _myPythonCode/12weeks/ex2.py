# -*- coding: utf-8 -*-
"""
Created on Mon May 20 10:24:05 2024

@author: irunn
"""

class Rabbit:
    shape = ""
    xPos = 0
    yPos = 0
    
    def __init__(self, value):
        self.shape = value

    def goto(self, x, y):
        self.xPos = x
        self.yPos = y        

rabbit1 = Rabbit("원")
print("토끼의 모양 :", rabbit1.shape)

rabbit2 = Rabbit("호랑이")
print("토끼의 모양 :", rabbit2.shape)
