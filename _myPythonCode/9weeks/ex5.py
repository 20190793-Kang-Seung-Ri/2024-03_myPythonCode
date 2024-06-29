# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 10:40:43 2024

@author: irunn
"""

import random

def lotto():
    list = []
    
    for i in range(6):
        num = random.randint(1, 45)
        
        if num not in list:
            list.append(num)
    
    return list

lottoList = lotto()
print("오늘의 로또 번호는", lottoList)