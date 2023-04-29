maxElementArray = []
maxElement = 0
numberOfElements = int(input('Enter the size of the list'))

for z in range(0, numberOfElements, 1):
    arrayElement = int(input('Enter the numbers'))
    maxElementArray.append(arrayElement)

print(maxElementArray)
for z in range(numberOfElements-1):
    if maxElementArray[z+1] > maxElementArray[z]:
        maxElementArray[z] = maxElementArray[z+1]
        maxElement = maxElementArray[z]
    elif maxElementArray[z] > maxElementArray[z+1]:
        maxElementArray[z] = maxElementArray[z]
        maxElement = maxElementArray[z]
print('The largest number is ', maxElement)

#Sir's logic
#for x in array:
#    if (maxEle < x):
#        maxEle = x
#        pass