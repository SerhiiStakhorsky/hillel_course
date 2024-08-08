def rental_car_cost(d):
    price = 40
    total = price * d
    if d >= 7:
        total -= 50
    elif d >= 3:
        total -= 20
    return total

print(rental_car_cost(8))