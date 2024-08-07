def find_quadrants(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and  y < 0:
        return  3
    elif x > 0 and y < 0:
        return 4

print(find_quadrants(1, 2))
print(find_quadrants(3, 5))
print(find_quadrants(-10, 100))
print(find_quadrants(-1, -9))
print(find_quadrants(19, -56))
