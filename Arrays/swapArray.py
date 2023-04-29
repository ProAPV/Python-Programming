arrayToBeSwapped = []
numberOfElementsInArray = int(input('Enter the number of elements'))
z = numberOfElementsInArray
temp = 0
for z in range(numberOfElementsInArray):
    element = int(input('Write the numbers of the arrays'))
    arrayToBeSwapped.append(element)

for z in range(int(numberOfElementsInArray/2)):
    temp = arrayToBeSwapped[z]
    arrayToBeSwapped[z] = arrayToBeSwapped[numberOfElementsInArray-z-1]
    arrayToBeSwapped[numberOfElementsInArray-z-1] = temp
print(arrayToBeSwapped)