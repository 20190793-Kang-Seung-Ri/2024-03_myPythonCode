# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:49:35 2024

@author: irunn
"""

import sys
pin = "1234"

class BankAccount:
    ownerName = ""
    balance = 0
    
    def __init__(self, value1, value2):
        self.ownerName = value1
        self.balance = value2
    
    def deposit(self, amount):
        self.balance += amount
        
        print(f"통장에 {amount}원이 입급되었습니다. ")
        
    def withdraw(self, amount):
        if self.balance < amount:
            print("잔액이 부족합니다. ")
            return
        
        self.balance -= amount
        
        print(f"통장에 {amount}원이 출금되었습니다. ")
        
    def getBalance(self):
        print(f"통장 잔액은 {self.balance}원 입니다. ")
        
    def getName(self):
        print(f"예금주 : {self.ownerName}")
        
userPin = input("비밀번호 : ")

if pin != userPin:
    print("비밀번호가 틀렸습니다. ")
    sys.exit()

account1 = BankAccount("홍길동", 100000)
account1.getName()
account1.getBalance()

while True:
    menu = input("1 - 잔액확인 / 2 - 출금 / 3 - 입금 / 4 - 종료 : ")
    
    if menu == '1':
        account1.getBalance()
    elif menu == '2':
        amount = int(input("출금할 금액 입력 : "))
        account1.withdraw(amount)
        account1.getBalance()
    elif menu == '3':
        amount = int(input("입금할 금액 입력 : "))
        account1.deposit(amount)
        account1.getBalance()
    elif menu == '4':
        sys.exit()
    else:
        continue
    
    print("-" * 30)
    print()