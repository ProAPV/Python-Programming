minArray = []
sizeOfArray = int((input("Enter the size of Array: ")))
for x in range(0, sizeOfArray):
    numbers = int(input("Enter the numbers for finding the minimum element: "))
    minArray.append(numbers)
minElement = minArray[0]
for x in range(0, sizeOfArray):
    
    if minElement > minArray[x]:  # 1 > 2 > 3 >4 >5
        minElement = minArray[x]  
print(minElement)