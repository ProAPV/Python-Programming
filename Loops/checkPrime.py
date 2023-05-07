#Python Program to Check Prime Number
#If it has only 2 factors number itself and 1.


prime = int(input("Enter the number"))
actualPrime = prime

if actualPrime != 1:
    for prime in range(2, prime):
        if actualPrime%prime==0:
            check = False
            break
        else:
            check = True

else:
     print(1, "is a unique number.")

if check == True:
    print(actualPrime, ("is a prime number."))
elif check == False:
    print(actualPrime, ("is not a prime number."))