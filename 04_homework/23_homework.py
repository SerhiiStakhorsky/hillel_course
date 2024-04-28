import random
lst1 = ()
add_element = random.randint(3, 10)
lst2 = [random.randint(1, 100) for i in range(add_element)]
lst3 = [lst2[1], lst2[3], lst2[-2]]
print(lst2, "==", lst3)
