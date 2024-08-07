import math
num1 = int(input("Print first number: "))
num2 = int(input("Print second number: "))
num3 = int(input("Print third number: "))

max = num1 if (num1 > num2 and num1 > num3) else (num2 if num2 > num3 else num3)
min = num1 if (num1 < num2 and num1 < num3) else (num2 if num2 < num3 else num3)

print(f"Max: {max}")
print(f"Mim: {min5}")
