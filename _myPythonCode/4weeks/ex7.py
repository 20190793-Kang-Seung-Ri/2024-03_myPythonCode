# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:04:53 2024

@author: irunn
"""

score = int(input("점수를 입력하세요 : "))

if score >= 100:
    grade = "A"
else:
    if score >= 80:
        grade = "B"
    else:
        if score >= 70:
            grade = "C"
        else:
            if score >= 60:
                grade = "D"
            else:
                grade = "F"

print("점수는 {}점 등급은 {}입니다. ".format(score, grade))
