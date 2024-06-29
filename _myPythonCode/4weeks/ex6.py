# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:37:08 2024

@author: irunn
"""

num = int(input("정수를 입력하세요 : "))

if num > 100:
    if num < 1000:
        print("{}은(는) 100보다 크고 1000보다 작습니다. ".format(num))
    else:
        print("{}은(는) 1000보다 큽니다. ".format(num))
else:
    print("{}은(는) 100보다 작습니다. ".format(num))
