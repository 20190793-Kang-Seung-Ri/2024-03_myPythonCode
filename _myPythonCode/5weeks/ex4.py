# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:46:36 2024

@author: irunn
"""

coffee = 5

while True:
    if coffee == 0:
        print("판매중지")
        break;
    
    money = int(input("돈을 넣어주세요 : "))
    
    if money == 300:
        coffee -= 1
        print("커피 한 잔이 나왔습니다. ")
    if money > 300:
        coffee -= 1
        print("커피 한 잔이 나왔습니다. ")
        print("{}원 거스름돈".format(money - 300))
    if money < 300:
        print("커피 한 잔은 300원 입니다. ")
        print("{}원 돌려드리겠습니다. ".format(money))