array1 = []
sum = 0
sizeOfArray = int(input("Enter the size of the array: "))

for x in range(0, sizeOfArray):
    numbers = int(input("Enter the numbers of the Array"))
    array1.append(numbers)

for x in range(0, sizeOfArray):
    sum += array1[x]
print(sum)