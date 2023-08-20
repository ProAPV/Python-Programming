# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.
# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Example Output
# Michael is going to buy the meal today!

import random

people = str(input("Enter the names of the people with a ',' and a space in between"))
names = people.split(", ")
nameIndex = random.randint(0, len(names)-1)
print(names[nameIndex], "is going to buy the meal today!")