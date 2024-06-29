# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:52:02 2024

@author: irunn
"""

height = float(input("신장(Cm) 입력: "))
weight = float(input("체중(Kg) 입력: "))

stdWeight = (height - 100) * 0.9

bmi = ((weight - stdWeight) / stdWeight) * 100

print("키(Cm) : {}".format(height))
print("체중(Kg) : {}".format(weight))
print("표준체중(Kg) : {}".format(stdWeight))
print("비만도(%) : {}".format(round(bmi, 2)))
