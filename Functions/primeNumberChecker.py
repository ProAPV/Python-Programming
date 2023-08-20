# Instructions
# Prime numbers are numbers that can only be cleanly divided by themselves and 1.

# https://en.wikipedia.org/wiki/Prime_number

# You need to write a function that checks whether if the number passed into it is a prime number or not.

# e.g. 2 is a prime number because it's only divisible by 1 and 2.

# But 4 is not a prime number because you can divide it by 1, 2 or 4.

prime = int(input("Enter the number which you want to check if it is a prime number or not"))
isPrime = True
x = 2

while prime%x==0 or x==prime-1:
    x+=1
    if prime%x == 0:
        isPrime = False
        break
    elif prime%x != 0:
        isPrime = True

if isPrime == True:
    print("It is a prime number")
else:
    print("It is not a prime number")