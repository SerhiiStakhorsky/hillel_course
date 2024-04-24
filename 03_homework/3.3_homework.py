lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = [1, 2, 3, 4, 5]
lst3 = []
lists = [lst1, lst2, lst3]
for lst in lists:
    if len(lst) % 2 == 1:
        x = lst[:len(lst) // 2 + 1]
        y = lst[1 + len(lst) // 2:]
    elif len(lst) % 2 == 0:
        x = lst[:len(lst) // 2]
        y = lst[len(lst) // 2:]
    else:
        x = lst
        y = []
    lst4 = [x, y]
    print(lst4)
