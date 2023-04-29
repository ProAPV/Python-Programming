mainList = []
sizeOfList = int(input("Enter the size of the list: "))
secondMaxElement = 0

for x in range(0, sizeOfList):
    numbers = int(input("Enter the numbers: "))
    mainList.append(numbers)

print(mainList)

maxElement = mainList[0]
secondMaxElement = mainList[0]

for x in range(0, sizeOfList-1):
    if maxElement < mainList[x+1]:
        maxElement = mainList[x+1]
    elif secondMaxElement < mainList[x+1] & mainList[x+1] < maxElement :
        secondMaxElement = mainList[x+1]
    
print("Second max element is: ", secondMaxElement)