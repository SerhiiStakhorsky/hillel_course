while True:
    try:
        input_number = int(input("Input five-digit number:"))
        if len(str(input_number)) != 5:
            print("It's not a five digit number")
            continue
        else:
            print("Your number is", input_number)
            x = (((input_number % 10) // 1) * 10000 +
                 ((input_number % 100) // 10) * 1000 +
                 ((input_number % 1000) // 100) * 100 +
                 ((input_number % 10000) // 1000) * 10 +
                 ((input_number // 10000)))
            print("Reverse number = ", x)
            break
    except ValueError:
        print("It's not a number")