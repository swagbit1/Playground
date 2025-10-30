amountDue = 50
change = 0
total = 0

while True:
    
    print(f"Amount Due: {amountDue - total}")
    user = int(input("Insert Coin: "))

    while user != 5 and user != 10 and user != 25:
        print(f"Amount Due: {amountDue - total}")
        user = int(input("Insert Coin: "))

    total += user
    if total >= amountDue:
        change = total - amountDue
        break

print(f"Change due {change}")
    