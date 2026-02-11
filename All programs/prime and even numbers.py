# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 15:18:47 2025

@author: CITD
"""

#To find given number is even or odd
a=int(input("Enter number to chech whether it is even or odd number = "))
if a % 2 ==0:
    print("The given number is Even number2")
else:
    print("The given number is Odd number")
    

# To check the number is prime or composite
a=int(input("Enter number to chech whether it is prime or composite number = "))
if a<= 1:
    print("Given number is not a prime number")
else:
    for i in range(2,a):
        if a%i == 0:
            print("The given number is composite number")
            break
    else: 
        print("The number is a Prime number")