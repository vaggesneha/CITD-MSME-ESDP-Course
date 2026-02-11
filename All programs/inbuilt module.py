# Inbuilt modules 
import math as a
b= a.floor(5.3)
c= a.factorial(9)
d= a.fabs(24)
e= a.sqrt(5)

'''
print(b,c,d,e)

import sys
print(sys.builtin_module_names) # to know all the inbuilt funvtiond
print(sys.modules.keys()) #list currently imported modules
help('module') # all modules with current modules'''

                                                       
''' 
import random
print(random.random())
print(random.randint(1,100)) #gives a random integer
print(random.randrange(1,100,20)) #within the range
nums = [1,4,5,7,8]
#choices
print(random.choices(nums, k=3))  # picks random numbers with size 3 and may repeated
#Samples
print(random.sample(nums, 3)) #without repeatation
#Shuffles
random.shuffle(nums)
print(nums) 
#Uniform
print(random.uniform(2.7,4.6)) # random float number between a and b
#Seed
random.seed(40) # python starts generating random numbers from fixed satrting point5
print(random.randint(1,100))
'''

#Statistics
'''
import statistics
data = [10,20,30,40,50]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.mode(data))
print(statistics.variance(data))
print(statistics.stdev(data))  #standard deviation
print(statistics.pstdev(data))  #populaation standard deviation
print(statistics.pvariance(data)) #population variance
'''

#Array (slower, needs more memory, adn different types are allowed)
'''
import array
a= array.array('i',[1,2,3,4,5,6])  # we can use 'f','d', 'u' for unicode character
print(a)
print(a.append(4))
print(a.insert(7,8))
print(len(a))
a[6] =10   #update the array
print (a)
'''

#String
import string
ls="A cat is sat on a table"
print (string.ascii_letters(ls))
print(string.ascii_lowercase(ls))
print(string.ascii_uppercase(ls))
print(string.digits(ls))
print(string.punctuation(ls))
print(string.whitespace(ls))

#operations
ch ='A'
if ch in string.ascii_letters:
    print("letters")
    
chars = string.ascii_letters + string.digits
print(chars)

r= "hello motto"
for p in string.punctuation:
    text=r.replace(p, "")
print(r)









