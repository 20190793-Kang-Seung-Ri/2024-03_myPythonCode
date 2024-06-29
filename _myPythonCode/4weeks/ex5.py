# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:32:13 2024

@author: irunn
"""

num = int(input("정수를 입력하세요 : "))

if num % 2 == 0:
    print("{}은(는) 짝수입니다. ".format(num))
else:
    print("{}은(는) 홀수입니다. ".format(num))
