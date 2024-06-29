# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:33:18 2024

@author: irunn
"""

level = int(input("레벨 : "))
local = input("지역주민 여부(Y/N) : ")

if level == 1:
    classs = "물개반"
    dc = 50000 * 0.2
elif level == 2:
    classs = "돌고래반"
    dc = 50000 * 0.15
elif level == 3:
    classs = "상어반"
    dc = 50000 * 0.1

sel = 50000 - dc

if local.upper() == 'Y':
    dc += 10000
    sel -= 10000

print("\n수강반 :", classs)
print("지역주민 여부(Y/N) :", local)
print("할인률 :", int(dc))
print("수강료 :", int(sel))
