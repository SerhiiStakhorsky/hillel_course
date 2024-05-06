input_number = int(input("Введіть число від  0 до 8640000: "))
if 0 <= input_number <= 8640000:
    days, seconds = divmod(input_number, 24*60*60)
    hours, seconds = divmod(seconds, 60*60)
    minutes, seconds = divmod(seconds, 60)

    if all((days % 10 ==1, days % 100 != 11)):
        words = "день"
    elif all((2 <= days % 10 <= 4,
          any((days % 100 < 10, days % 100 >= 20)))):
        words = "дні"
    else:
        words = "днів"
    print(f"{days} {words}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
else:
    print("Число не входить в діапазон значень.")
