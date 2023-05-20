#Write a program that works out whether if a given year is a leap year.
#A normal year has 365 days, leap years have 366, with an extra day in
#February. The reason why we have leap years is really fascinating, 
#this video does it more justice:

leapYr = int(input("Enter to check"))

if leapYr%400==0 and leapYr%100==0: #2020%400 != 0 if terminated
    check = True
elif leapYr%4==0 and leapYr%100!=0: #2020%4=0==0 && 2020%100=20!=0 True 
    check = True                  #whole loop terminated and check == True
else:
    check = False

if check == True:
    print(leapYr, "is a leap year")
elif check == False:
    print(leapYr, "is not a leap year")
else:
    print(leapYr, "is an invalid year")