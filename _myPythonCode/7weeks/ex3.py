# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:31:38 2024

@author: irunn
"""

store = {}

while True:
    item = input("입력 물품 : ")
    
    if item == "":
        break;
    
    count = int(input("재고량 : "))
    
    store[item] = count

print("*** 물품 재고량 확인 ***")

while True:
    item = input("찾을 물품 : ")
    
    if item == "":
        break;
    
    if item in store:
        print(f"{store[item]}개 남았습니다. ")
    else:
        print("그 물품은 없습니다. ")
