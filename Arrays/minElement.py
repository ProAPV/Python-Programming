minArray = []
minElement = 0
sizeOfArray = int((input("Enter the size of Array: ")))
for x in range(0, sizeOfArray):
    numbers = int(input("Enter the numbers for finding the minimum element: "))
    minArray.append(numbers)
for x in range(0, sizeOfArray):
    print(x)
    print('x')
    print(minElement)
    if minElement > minArray[x]:  
        print(minElement)      # 1 > 2 > 3 >4 >5
        minElement = minArray[x]        #pass
        pass
print(minElement)