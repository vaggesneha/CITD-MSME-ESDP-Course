# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 13:37:12 2025

@author: CITD
"""
#Pattern1
a= int(input("Enter the number of rows:"))
for i in range(a):
    for b in range(a-i-1):
        print("   ",end="   ")
    for b in range(3*i+1):
        print("*",end="   ")
    print()
    
    
#Pattern2
a= int(input("Enter the number of rows:"))
for i in range(a-1, -1, -1):
    for b in range(a-i-1):
        print("   ",end="   ")
    for b in range(3*i+1):
        print("*",end="   ")
    print()

    
#Patttern3    Complete image
a= int(input("Enter the number of rows for combined pattern:"))
for i in range(a):
    for b in range(a-i-1):
        print("   ",end="   ")
    for b in range(3*i+1):
        print("*",end="   ")
    print()


for i in range(a-2, -1, -1):
    for b in range(a-i-1):
        print("   ",end="   ")
    for b in range(3*i+1):
        print("*",end="   ")
    print()
    
    
    
#Pattern4 Christmas Tree
a= int(input("Enter the number of rows for christmas tree:"))
for part in range(3):
    for i in range(a):
        for b in range(a - i - 1):
            print(" ", end=" ")
        for b in range(3*i + 1):
            print("*", end=" ")
        print()
for i in range(2):
    for b in range(a-1):
        print(" ",end=" ")
    print("* * *")
 
 
 
 
 
 
    