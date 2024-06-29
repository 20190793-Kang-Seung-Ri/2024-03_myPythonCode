# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 09:29:53 2024

@author: irunn
"""

def fact(n):
    sum = 1
    
    for i in range(1, n + 1):
        sum *= i
        
    return sum

k = fact(5)
print(f"5! = {k}")