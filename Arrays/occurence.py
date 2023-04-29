inputArray = []
finalOccurence = 0
sizeOfArray = int(input("Enter the size of the Array: "))

for x in range(0, sizeOfArray):
    numbers = int(input("Enter the numbers of the array"))
    inputArray.append(numbers)

occurence =inputArray[0]
numberToBeFound = int(input("Enter the number for finding its occurence: "))

for x in range(0, sizeOfArray):
    if numberToBeFound == inputArray[x]:
        finalOccurence+=1
        pass

print("The occurence of ", numberToBeFound, "is ")
print(finalOccurence)