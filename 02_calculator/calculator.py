# Get user input
def get_number(position):
    while True:
        operand = input(f"Enter {position} number: ")
        try:
            return float(operand)
        except:
            print("Invalid input! Please enter a valid number.")

operand = get_number('first')
operand2 = get_number('second')
sign_list = ["+", "-", "*", "/"]
sign = input("Sign (+, -, *, /): ")
operation = None
final_operation = None


# Validate operator
while sign not in sign_list:
    print("Invalid sign! Please enter a valid sign.")
    sign = input("Sign (+, -, *, /): ")

# Handle division by zero
if sign == "/":
    while operand2 == 0:
        print("You can't divide by zero!")
        operand2 = float(input("Enter a valid second number: "))

# Perform calculation
if sign == "+":
    result = operand + operand2
    operation = "Addition"
    final_operation = f"{operation} of {operand} and {operand2}"
elif sign == "-":
    result = operand - operand2
    operation = "Subtraction"
    final_operation = f"{operation} {operand2} from {operand}"
elif sign == "*":
    result = operand * operand2
    operation = "Multiplication"
    final_operation = f"{operation}  of {operand} by {operand2}"
elif sign == "/":
    result = operand / operand2
    operation = "Division"
    final_operation = f"{operation}  of {operand} by {operand2}"

# Display the result
print(f"{final_operation} = {result}")
print("*********************************************")  
        