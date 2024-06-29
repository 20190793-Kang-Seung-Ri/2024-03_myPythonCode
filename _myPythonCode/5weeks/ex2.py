# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:49:13 2024

@author: irunn
"""

for dan in range(2, 10, 1):
    print("=== {}단 ===".format(dan))
    for i in range(1, 10):
        print("{} * {} = {}".format(dan, i, dan * i))
    print(" ")
