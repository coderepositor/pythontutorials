""" Ask user the year to enter and write a program to validate the year entered
is leap year or not """

year = int(input("enter the year - "))
#print(year, type(year))
"""
conditions to check the year is leap year
1. Year should be divisible 400
2. Year shouldn't be divisible by 100
3. Year should by divisble by 4
"""
"""
if(year%400 == 0):
    print(year," is a leap year")
else:
    if(year%100 != 0):
        if(year%4==0):
            print(year," is a leap year")
        else:
           print(year," is not a leap year")
    else:
        print(year," is not a leap year")
        
"""
"""
if(year%400 == 0):
    print(year," is a leap year")
elif(year%100 !=0 and year%4 == 0):
    print(year," is a leap year")
else:
    print(year," is not a leap year")
"""

if(year%400 == 0 or (year%100!=0 and year%4==0)):
     print(year," is a leap year")
else:
     print(year," is not a leap year")
     












