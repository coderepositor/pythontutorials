import math

"""
Ashish has decided to take out a 30-Year fixed rate mortgage loan of Rs.600,000
with RBL Bank, Bajaj Finance and Bitcoin trading corporation. The interest rate
is 5% and the montly payment is 2684.11

Calculate the total amount that Ashish will have to pay over the life of the
mortgage
"""

principal = 600000.000
rate = 0.05
payment = 2185.11666
total_paid = 0.0
while principal > 0:
    principal = principal*(1+rate/12) - payment
    total_paid += payment;
#print("Total Paid ", math.ceil(total_paid))
#print("Total Paid ", math.floor(total_paid))
#print("Total Paid ", round(total_paid,6))
#print("Total Paid ", round(total_paid,3))

print(math.factorial(5))
