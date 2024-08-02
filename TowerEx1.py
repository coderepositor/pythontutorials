""" Problem
    One morning you go out and place a dollar bill on the sidewalk by the UST Tower in
    Trivendrum. Each day thereafter you go out double the number of bills. How long
    does it take for the stack of bills to exceed the height of tower,
    if the  the tower height i s 442m.
    bill  thickness is 0.11m
"""
bill_thickness = 0.11
tower_height = 422
no_of_bills = 1
days = 1

while(no_of_bills*bill_thickness < tower_height):
    days+=1;
    no_of_bills *= 2

print("no  of days: ", days)
print("no of bills: ",no_of_bills)
print("Final height of bills: ", no_of_bills * bill_thickness)
