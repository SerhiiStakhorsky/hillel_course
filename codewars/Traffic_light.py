def update_light(current):
    trafick_light = ["green", "yellow", "red"]
    if current in trafick_light:
        index = trafick_light.index(current)
        next_light = trafick_light[(index+1) % len(trafick_light)]
        return  next_light
    else:
        print("Invalid light")

current = input("Input current light: ")
print(update_light(current))