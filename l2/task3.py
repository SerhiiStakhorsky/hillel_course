lst = [1, True, "hello", 5.4, 5]
if 5 or "hello" in lst:
    print("5 and 'hello' - is in list")
else:
    print("5 and 'hello' - isn't in list")

lst[lst.index(5)] = 50
print(lst)

