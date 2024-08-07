import math

def input_float(prompt):
    while True:
         try:
            return float(input(prompt))
         except ValueError:
            print("Это не число")


n1 = input_float("Введите первое число: ")
n2 = input_float("Введите второе число: ")
print(n1)
print(n2)

print(f"Сумма: {n1 + n2}")
print(f"Разница: {n1 - n2}")
print(f"перемножение: {n1 * n2}")
try:
    print(f"Деление: {n1 / n2}")

except ZeroDivisionError:
    print("Нельзя делить на 0")

print(f"Квадратный корень из {n1} и {n2} = {math.sqrt(n1 +n2)}")
if n1.is_integer() and n1 >=0:
    print(f"Факториал первого числа: {math.factorial(int(n1))}")
else:
    print("Invalid number")