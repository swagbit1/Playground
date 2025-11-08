import random 

steps = 10
urn = [1,2]

for i in range(steps):
    choice = random.choice(urn)

    if choice == 1:
        urn.append(1)
    elif choice == 2:
        urn.append(2)

print(urn[:5])
print(f"1 Count: {urn.count(1)},  {(urn.count(1)/len(urn)) * 100:.2f}%\n2 Count: {urn.count(2)},   {(urn.count(2)/len(urn)) * 100:.2f}%")



def fac(n):
    if n == 0:
        return 1
    
    if n == 1:
        return 1
    
    return n * fac(n - 1)

print(f"Prob of such sequence: {((fac(urn.count(1)) * fac(urn.count(2)))/fac(len(urn))) * 100:.2f}%")