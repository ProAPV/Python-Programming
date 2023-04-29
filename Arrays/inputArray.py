#Take the size of the array from the user and take the list
#elements for input by the user. Then print the array.

arr = []
noe = int(input('Enter the size of arr'))
for a in range(0, noe):
    ele = int(input('Enter the list elements of the array'))
    arr.append(ele)
print(arr)