while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter next number: "))
    operation = input("Enter operation (+, -, *, /): ")
    if operation == "+":
        num1 = num1 + num2
    elif operation == "-":
        num1 = num1 - num2
    elif operation == "*":
        num1 = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("The numbers are not divisible by zero")
            continue
        else:
            num1 = num1 / num2
    else:
        print("Invalid operation")
        continue
    print("Current result: ", num1)
    check_continue = input("Do you want to continue (yes/no): ")
    if check_continue.lower() not in ["yes", "y"]:
        break
print("Final result:", num1)
