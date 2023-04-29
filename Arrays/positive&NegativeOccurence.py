mainList = []
sizeOfList = int(input("Enter the size of the list: "))
Positive = 0
Negative = 0
Zero = 0

for x in range(0, sizeOfList):
    numbers = int(input("Enter the numbers of the list: "))
    mainList.append(numbers)

for x in range(0, sizeOfList):
    if mainList[x] > 0:
        Positive += 1
    elif mainList[x] < 0:
        Negative += 1
    else:
        Zero += 1

print("The numbers of Positive numbers in the list are", Positive)
print("The numbers of Negative numbers in the list are", Negative)
print("The numbers of Zero's in the list are", Zero)