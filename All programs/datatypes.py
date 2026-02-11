# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 14:48:56 2025

@author: CITD
"""

#Data types (numerical, boolean, string, sequence)
#Numerical
a = input("Enter the number to check : ")
if '.' in a:
    print("is a float type")
elif a.isdigit():
    print( "is a int type")
elif "j" in a:
    print( "is a complex type")
else:
    print("Invalid number")


#Boolean
b = int (input("Enter the number to check : "))
if b % 5 == 0:
    print(True)  # boolean type
else:
    print(False)
    
#string
c = str(input("Enter the string you want to display : "))
print(c)

#sequence
lst = [1, 3,7 ,2,4,5,7,2,3,2,6j,"python"] #ordered & mutable
print(lst)
tpl =(1,2,3,4,6 ,"hello",[1,23,34,7,8,12]) # ordered & non mutable
print(tpl)
set={1,2,8,"world", 7j} #unordered & mutable
print(set)