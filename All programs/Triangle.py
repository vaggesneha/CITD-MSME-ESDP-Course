# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 14:35:20 2025

@author: CITD
"""

#Constructing a traingle according to the userdefine
a = int(input("enter the one side value a= "))
b = int(input("enter the second side value b= "))
c = int(input("enter the third side value c= "))
#Check condition for valid triangle
if a + b >c and  a + c > b and  b + c > a:
    print("The values are valid!")
else:
    print("Please enter a correct values")
    
if a==b==c:
    print("For given side values, an Equalateral triangle is formed")

elif a**2 + b **2 > c**2:
    print ("It is a  scalene triangle")
else:
    print ("It is a isosceles triangle")
    
    
        
        
        
