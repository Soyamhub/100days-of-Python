def add(n1, n2):
    return n1+n2

def substract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations = {
    '+' : add,
    '-' : substract,
    '*' : multiply,
    '/' : divide
}

import art

def calculator():
    print(art.logo)
    num1 = float(input("Enter the first number: "))

    for symbols in operations:
        print(symbols)


    again = True
    while again:

        operation_symbol = input("Pick an operation from above: ")
        num2 = float(input("Enter the next number: "))

        operation_function = operations[operation_symbol]
        answer = operation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")  


        new_operation = input("Type 'y' to continue calculating with " +  str(answer) + ", or type 'n' to exit.: ").lower()
        if new_operation == 'y':
            num1 = answer
        else:
            again = False
            print("\n")
            calculator()

calculator()
     