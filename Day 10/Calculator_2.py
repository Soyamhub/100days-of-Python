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

num1 = int(input("Enter the first number: "))

for symbols in operations:
    print(symbols)

operation_symbol = input("Pick an operation from above: ")

num2 = int(input("Enter the second number: "))

operation_function = operations[operation_symbol]
first_answer = operation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")  


operation_symbol = input("Pick another symbol: ") 
num3 = int(input("Enter the second number: ")) 
operation_function = operations[operation_symbol]
second_answer = operation_function(first_answer, num3) 

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")   