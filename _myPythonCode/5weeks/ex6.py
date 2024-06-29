# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 12:29:20 2024

@author: irunn
"""

while True:
    num1 = int(input("첫번째 정수 : "))
    num2 = int(input("두번째 정수 : "))

    if num1 == 0 and num2 == 0:
        break;

    if num1 < num2:
        num1, num2 = num2, num1

    while True:
        rem = num1 % num2

        if rem == 0:
            break;

        num1 = num2
        num2 = rem
    
    print("최대공약수는 {}입니다. ".format(num2)) 

