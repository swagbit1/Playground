import random 

steps = 200000000
urn = [1,2]

for i in range(steps):
    choice = random.choice(urn)

    if choice == 1:
        urn.append(1)
    elif choice == 2:
        urn.append(2)

print(urn[:5])
print(f"1 Count: {urn.count(1)},  {(urn.count(1)/len(urn)) * 100:.2f}%\n2 Count: {urn.count(2)},   {(urn.count(2)/len(urn)) * 100:.2f}%")
    