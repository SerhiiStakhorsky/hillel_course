lst1 = (0, 1, 0, 12, 3)
lst2 = (0,)
lst3 = (1, 0, 13, 0, 0, 0, 5)
lst4 = (9, 0, 7, 31, 0, 45, 0, 0, 96, 0)
lists = [lst1, lst2, lst3, lst4]
processed_lists = []
for lst in lists:
    non_zeros = [x for x in lst if x != 0]
    zeros = [x for x in lst if x == 0]
    processed_lists.append(non_zeros + zeros)
for lst in processed_lists:
    print(lst)
