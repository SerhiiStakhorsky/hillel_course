num1 = int(input("1 element: "))
num2 = int(input("2 element: "))
num3 = int(input("3 element: "))
num4 = int(input("4 element: "))
num5 = int(input("5 element: "))

lst = [num1, num2, num3, num4, num5]
lst.sort()
print(lst)
sum = sum(lst)
print(sum)
