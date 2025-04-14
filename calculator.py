def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b


def operations(digit1, operator_symbol, digit2):
    if operator_symbol == "+":
        return addition(digit1, digit2)
    elif operator_symbol == "-":
        return  subtraction(digit1, digit2)
    elif operator_symbol == "*":
        return  multiplication(digit1, digit2)
    elif operator_symbol == "/":
        return  division(digit1, digit2)
    else:
        return "invalid operator"


calculating = True
while calculating:
    num1 = float(input("What's the first number?: "))
    operators = input("+\n-\n*\n/\nPick an operator: ")
    num2 = float(input("What's the next number?: "))
    answer = operations(num1, operators, num2)
    print(f"Result: {num1} {operators} {num2} = {answer}")

    continuing = True
    while continuing:
        choice = input(f"Type 'y' to continue calculating with {answer},"
              f" or type 'n' to start a new calculation \nor 'exit' to end calculator: ")
        if choice == "y":
            operators = input("+\n-\n*\n/\nPick an operator: ")
            next_num = float(input("What's the next number?: "))
            answer = operations(answer, operators, next_num)
            print(f"Updated result: {answer}")
        elif choice == "n":
            continuing = False
        elif choice == "exit":
            print(f"Your final answer is {answer}")
            continuing = False
            calculating = False
        else:
            print("Invalid input. Please type 'y', 'n', or 'exit'.")
