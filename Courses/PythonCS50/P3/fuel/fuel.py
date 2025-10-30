while True:
    try:
        x, y = input("Fraction: ").split("/")
        x, y = int(x), int(y)

        if x > y or y == 0:
            continue

        fuel = round((x / y) * 100)
        break

    except (ValueError, ZeroDivisionError):
        continue

if fuel >= 99:
    print("F")
elif fuel <= 1:
    print("E")
else:
    print(f"{fuel}%")
