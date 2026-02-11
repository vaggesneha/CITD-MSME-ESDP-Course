#Finding a leap year
a = int(input("Enter the year to know whether the it is leap year or not : "))
if a % 4 == 0 and a % 100 == 0:
    print("The given year is leap year ")
else:
    print("The given year is not a leap year")
    

# To check which year is a leap year
year = int(input("Enter the year present year to find when is the next leap year : "))
while year % 4 != 0 and year % 100 != 0 :
    year= year + 1

print (year,"is a next leap year")
    
    
# To find the leap year with month
m = int(input("Enter the month (choose 1-12) : "))
y= int(input("Enter the year : "))
if y % 4 == 0 and y % 100 == 0:
    leap = True
else:
    leap = False
# For month
if m in [1,3,5,7,8,10,12]:
    print("31 days")
elif m in [4,6,9,11]:
    print("30 days")
elif m in [2]:
    if leap:
        print("29 days (leap year)")
    else:
        print("28 days (not a leap year)")
else:
    print("Invalid month")