# Task 1

# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.

# Perform the calculation and display the result.


print("=== Simple Calculator ===")
print("Operations: +  -  *  /")

# Taking inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

# Performing calculation
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation!"

# Display result
print("Result:", result)
