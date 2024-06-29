# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:25:31 2024

@author: irunn
"""

menus = {"돈가스" : 5000, 
         "생선가스" : 5500, 
         "우동" : 2500, 
         "초밥세트" : 9000}

for menu, price in menus.items():
    print(menu, ":", price, "원")