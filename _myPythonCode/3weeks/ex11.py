# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:02:14 2024

@author: irunn
"""

won = int(input("환전할 금액(원) : "))

print("환전 금액 : {}원".format(won))
print("미국 : {}USD".format(won // 1228))
print("잔액 : {}원".format(won % 1228))