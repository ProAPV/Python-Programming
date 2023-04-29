palindrome = str(input("Enter the number to check its palindrome"))
length = (len(palindrome))/2
if length%2 != 0:
    length = length+0.5
    pass
for x in range(int(length)):
    if palindrome[:x] == palindrome[:int(length-1):-1]:
        check = True
    else:
        check = False
if check == True:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome.")

    # Check whether the string is palindrom or not
palindrome = ""
palindrome = str (input ("enter the string"))
length = len(palindrome)
flag = 0

for x in range (0, int(length/2)):
        if palindrome[x] == palindrome[length -x-1]:
            continue
        else:
            flag = 1
            break

if (flag == 1):{
    print("%s is not palindrome"%palindrome)
}
else :{
    print("%s is a palindrome"% palindrome)
}