# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 11:58:32 2025

@author: CITD
"""

#Operators
print("Hey there! Welcome to the testing of working of operators ")
print("Please select the number you want to perform an operation:\n", "1.Arithmetic operator\n", "2.Relational operator\n","3.Logical operator\n", "4.Bitwise operator\n","5.Membership operator\n","6.Identity Operator\n")

a= int(input("Select the number which operation you want to perform:"));
if a == 1:
    x = int(input("Enter the value of first value to perform arithmetic values: a= "))
    y = int(input("Enter the value of second value to perform arithmetic values: b= "))
b=int(input("Select the mode of operation you want to perform (1- Add, 2-Sub, 3-Mul, 4-Div ) : "))
if b == 1:
    print(x + y)
if b ==2:
    print( x - y)
if b== 3: 
    print( x * y)
if b == 4:
    print( x % y)
elif a == 2:
    if a> b:
        print(" a is greater than b")
        if a < b:
            print("b is greater the a")
            if a == b:
                print("a is equal to b")
elif a == 3:
    print("okay")
                
    
    
     