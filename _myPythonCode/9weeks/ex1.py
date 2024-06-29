# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 09:29:52 2024

@author: irunn
"""

def hap(a, b):
    sum = 0
    
    for i in range(a, b + 1):
        sum += i
        
    return sum

print(hap(1, 10))
print(hap(100, 200))
print(hap(3, 9))