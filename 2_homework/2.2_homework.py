input_number = int(input("Input five-digit number:"))
print("Your number is", input_number)
x = (((input_number % 10) // 1) * 10000 +
     ((input_number % 100) // 10) * 1000 +
     ((input_number % 1000) // 100) * 100 +
     ((input_number % 10000) // 1000) * 10 +
     ((input_number // 10000)))
print(x)