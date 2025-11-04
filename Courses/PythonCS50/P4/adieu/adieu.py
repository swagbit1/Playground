
names = []
try:
    while True:
        name = input("Name: ")
        names.append(name)
except EOFError:
    
    if len(names) < 2:
        print(f"Adieu, adieu to {name}")
    else:
        print("\nAdieu, adieu, to " + ", ".join(names[:-1]) + " and " + names[-1])
    