cal = {
    "apple": 130,
    "avacado": 50
    # To lazy to add more items
}

user = input("Item: ").lower()

if user in cal:
    print(f"Calories: {cal[user]}")