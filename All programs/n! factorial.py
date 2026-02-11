# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 11:41:14 2025

@author: CITD
"""
#TO FIND FACTORIAL
n = int(input("Enter the number to find factorial : "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)


#Permutation  npr= n!/(n-r)!
print("To find permutation , we need two values(n,r)")
n= int(input("Enter the value of n = "))
r = int(input("Enter the value of r = "))
n1 = 1
r1 = 1
for i in range(1, n + 1):
    n1 = n1 * i
for i in range(1, n - r + 1):
    r1 = r1 * i
permutation = n1//r1
print("Permutation = ", permutation)


#Combination (ncr = n!/r!(n-r)!)
print("To find combination , we need two values(n,r)")
n= int(input("Enter the value of n = "))
r = int(input("Enter the value of r = "))
n1 = 1
r1 = 1
nr = n1
for i in range(1, n + 1):
    n1 = n1 * i
for i in range(1, r + 1):
    r1 = r1 * i
for i in range(1, n - r + 1):
    nr = nr * i
combination = n1//r1 * nr
print("Combination = ", combination)
