def multiply_digits(number):
    while number > 9:
        digits = [int(digit) for digit in str(number)]
        product = 1
        for digit in digits:
            product *= digit
        number = product
        print(number, "-> ", product)
    return number


user_number = int(input("Print number: "))
print(multiply_digits(user_number))
