def problem(a):
    if isinstance(a, str):
        return "Error"
    else:
        return a * 50 + 6

a = int(input("Input number: "))
print(problem(a))
