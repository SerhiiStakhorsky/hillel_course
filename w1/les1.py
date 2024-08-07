try:
    user_number_1 = input("Input first number: ")
    user_number_2 = input("Input second number: ")
    n1 = float(user_number_1)
    n2 = float(user_number_2)

    print(f"Sum: {n1 + n2}")
    print(f"Difference: {n1 - n2}")
    print(f"Product: {n1 * n2}")
    print(f"Quotient: {n1 / n2}")

    div, mod = divmod(n1, n2)
    print(f"Integer division result: {div}")
    print(f"Remainder: {mod}")
except ValueError:
    print("Ошибка: введено нечисловое значение.")
except ZeroDivisionError:
    print("Ошибка: деление на ноль.")
