# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:21:45 2024

@author: irunn
"""

n = int(input("정수 입력 : "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1
        print(i, end = ' ')

print("\n약수의 갯수 :", count)

if count == 2:
    print("소수(prime number)")