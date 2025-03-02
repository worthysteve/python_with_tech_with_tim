# expression = input("Type an expression: ")
operand = input("Enter first number: ")
operand2 = input("Enter second number: ")
sign_list = ["+", "-", "*", "/"]
sign = input("Sign: ")

while sign not in sign_list:
    print("Invalid sign! please enter a valid sign.")
    sign = input("Sign: ")
    if sign == "+":
        result = float(operand) + float(operand2)
        print(f"Result: {result}")
    elif sign == "-":
        result = float(operand) - float(operand2)
        print(f"Result: {result}")
    elif sign == "*":
        result = float(operand) * float(operand2)
        print(f"Result: {result}")
    elif sign == "/":
        while operand2 == 0:
            print("You can't divide by zero!")
            operand2 = input("Enter a valid second number: ");
        result = float(operand) / float(operand2)
        print(f"Result: {result}")
    else:
        print("Invalid sign!")
    print("*********************************************");