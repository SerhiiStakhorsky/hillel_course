lst = [1, "cherry", 333, "apple", "banana", "6.0", 7, 81, 123]
y = len(lst)
lst.insert(0, lst[len(lst) - 1])
del lst[y]
print(lst)
