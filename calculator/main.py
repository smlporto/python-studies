def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}

def calculator():
    value1 = int(input("Choose the first number: "))
    for symbols in operations:
        print(symbols)

    keep_going = True

    while keep_going:
        operation_symbol = input("Choose one of the operations above: ")
        value2 = int(input(f"{value1} {operation_symbol} "))

        calculation = operations[operation_symbol]
        result = calculation(value1, value2)

        print(f"{value1} {operation_symbol} {value2} = {result}")

        answer = input(f"Keep calculating with {result}? ('y' / 'n') ")

        if answer != "y":
            keep_going = False
            calculator()
        else:
            value1 = result

calculator()
