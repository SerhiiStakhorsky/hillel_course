import random
lst1 = ()
add_element = random.randint(0, 9)
lst2 = [random.randint(1, 10) for i in range(add_element)]
if len(lst2) ==0:
    print(lst2, "=", 0)
else:
    summ_even_element = sum(lst2[i] for i in range(0, len(lst2), 2))
    final_result = summ_even_element * lst2[-1]
    print(lst2, "=", final_result)
