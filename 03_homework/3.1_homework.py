num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == "+":
    result = (num1 + num2)
elif operation == "-":
    result = (num1 - num2)
elif operation == "*":
    result = (num1 * num2)
elif operation == "/":
    if num2 == 0:
        print("The numbers are not divisible by zero")
    else:
        result = (num1 / num2)
else:
    print("Invalid operation")
print("Result: ", num1,operation, num2,"=", result)
