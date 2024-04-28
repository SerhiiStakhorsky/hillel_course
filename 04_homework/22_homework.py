import random
lst1 = ()
add_element = random.randint(2, 9)
lst2 = [random.randint(1, 10) for i in range(add_element)]
summ_even_element = sum(lst2[i] for i in range(0, len(lst2), 2))
last_element = lst2[-1]
final_result = summ_even_element * last_element
print(lst2, "=", final_result)
