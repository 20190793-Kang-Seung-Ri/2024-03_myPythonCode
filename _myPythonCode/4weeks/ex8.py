# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:11:19 2024

@author: irunn
"""

score = int(input("점수를 입력하세요 : "))

if score >= 100:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("점수는 {}점 등급은 {}입니다. ".format(score, grade))
