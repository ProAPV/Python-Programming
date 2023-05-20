#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

bill = int(input("Enter the total bill in dollars"))
ppl = int(input("Enter the number of people in which the bill has to be distributed."))
tip = int(input("Enter the tip you want to give in percentage"))

distributed =  bill/ppl
distributed = distributed
if tip == 0:
    print("The amount all", ppl, "have to pay is", distributed, "and the tip is 0")
elif tip != 0:
    finalTip = (distributed*tip)/100
    finalTip = ('%.2f' % finalTip)
    print("The amount all", ppl, "people have to pay is", ('%.2f' % distributed), "and the tip is", finalTip)    