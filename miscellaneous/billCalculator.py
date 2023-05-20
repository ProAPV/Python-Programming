#Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
#Based on a user's order, work out their final bill.
#Small Pizza: $15
#Medium Pizza: $20
#Large Pizza: $25
#Pepperoni for Small Pizza: +$2
#Pepperoni for Medium or Large Pizza: +$3
#Extra cheese for any size pizza: + $1

size = input("input the size S, M or L")
peproni = input("Write YFS for extra peperoni on small pizza and YFML for peperoni on large or medium pizza and N for no extra peperoni")
cheese = input("Write Y for extra cheese and N for no extra cheese")

bill = 0

if size == 'L':
    bill += 25
elif size == 'M':
    bill+= 20
elif size == 'S':
    bill+=15

if peproni == 'YFS':
    bill+=2
elif peproni == 'YFML':
    bill += 3

if cheese == 'Y':
    bill+=1

print("The total bill for your order is $", bill)