# Get user input
operand = input("Enter first number: ")
operand2 = input("Enter second number: ")
sign_list = ["+", "-", "*", "/"]
sign = input("Sign: ")

# Validate sign
while sign not in sign_list:
    print("Invalid sign! Please enter a valid sign.")
    sign = input("Sign: ")

# Perform calculations
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
    while operand2 == "0":
        print("You can't divide by zero!")
        operand2 = input("Enter a valid second number: ")

    result = float(operand) / float(operand2)
    print(f"Result: {result}")

print("*********************************************")