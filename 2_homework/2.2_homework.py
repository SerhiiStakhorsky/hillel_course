input_number = int(input("Input five-digit number:"))
print("Your number is", input_number)
print (input_number % 10 // 1,
       input_number % 100 // 10,
       input_number % 1000 // 100,
       input_number % 10000 // 1000,
       input_number // 10000)