def add(n1, n2):
    sum = n1+n2
    return sum

def substract(n1, n2):
    difference = n1-n2
    return difference

def multiply(n1, n2):
    product = n1*n2
    return product

def divide(n1, n2):
    if n2 == 0:
        quotient = "∞"
    else:
        quotient = n1/n2
    return quotient

operators = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

def calc():
    end = "c"
    n1 = int(input("Enter the number: "))
    inf = "∞"

    while end == "c" or end == "n":
        for symbols in operators:
            print(symbols)
        operation = input("Enter the symbol you want to use: ")
        n2 = int(input("Enter the number: "))
        result = operators[operation]
        finalResult = result(n1, n2)
        if finalResult != "∞":
            print(finalResult)
            end = str(input('Enter "c" to continnue or "e" to end or "n" to start a new calculation: '))
            n1 = finalResult
            if end == "n":
                calc()
        else:
            print(inf)
            break

calc()