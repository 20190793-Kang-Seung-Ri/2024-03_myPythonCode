# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 12:18:28 2024

@author: irunn
"""

n = int(input("정수 입력 : "))
flag = True

for i in range(2, n):
    if n % 2 == 0:
        flag = False
        break;

if flag == True:
    print("{}은 소수입니다. ".format(n))
else:
    print("{}은 소수가 아닙니다. ".format(n))