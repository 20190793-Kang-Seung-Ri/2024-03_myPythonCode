# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 09:17:19 2024

@author: irunn
"""

num1 = int(input("첫번째 정수 : "))
num2 = int(input("두번째 정수 : "))

sum = 0

if num1 > num2:
    num1, num2 = num2, num1
        
for i in range(num1, num2 + 1, 1):
    sum += i

print("{} ~ {}까지 정수의 합은 : {}".format(num1, num2, sum))
