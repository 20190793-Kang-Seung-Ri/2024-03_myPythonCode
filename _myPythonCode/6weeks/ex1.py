# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 09:09:30 2024

@author: irunn
"""

scores = [] # scores = list()
sum = 0

print("홍길동 선수 경기가 끝났습니다. ")

for i in range(5):
    jumsu = int(input("평가 점수 입력 : "))
    
    scores.append(jumsu)

for i in range(5):
    sum += scores[i]

print("심사위원 총점 : {}".format(sum))
print("심사위원 평균점수 : {}".format(round(sum / len(scores), 2)))
