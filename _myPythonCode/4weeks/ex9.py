# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:15:26 2024

@author: irunn
"""

code = int(input("직급코드(1 : 과장, 2 : 차장, 3 : 부장)를 입력하세요 : "))
income = int(input("총 소득(원)을 입력하세요 : "))

if code == 1:
    tax = income * 0.08
    job = "과장"
elif code == 2:
    tax = income * 0.12
    job = "차장"
else:
    tax = income * 0.18
    job = "부장"

pay = income - tax

print("직급 :", job)
print("총 소득(원) :", income)
print("세금 :", int(tax))
print("실수령액(원) :", int(pay))
