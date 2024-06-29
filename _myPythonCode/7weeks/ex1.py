# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:43:17 2024

@author: irunn
"""

singer = {"이름" : "트와이스", 
          "구성원수" : 9, 
          "데뷔" : "서바이벌 식스틴", 
          "대표곡" : "Cry For Me"}

for key in singer.keys():
    print(key, ":", singer[key])