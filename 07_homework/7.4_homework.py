
def common_elements():
    multiplies_to_5 = {x for x in range(100) if x % 5 == 0}
    multiplies_to_3 = {x for x in range(100) if x % 3 == 0}
    intersections = multiplies_to_5 & multiplies_to_3
    return intersections

if __name__ == "__main__":
    print(common_elements())