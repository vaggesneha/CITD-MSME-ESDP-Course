# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 11:28:11 2025

@author: CITD
"""


#Fibonacci series
n= int(input("Enter the number of terms (n): "))

a= 0
b=1
for i in range(n):
    print(a, end = " ") # keeps numbers on same line
    c= a+ b
    a = b # moves to next next , where old a becomes new b 
    b = c #  and old b becomes new c