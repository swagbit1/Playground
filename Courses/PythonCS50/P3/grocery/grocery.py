gro = {}

while True:
    try:
        user = input("").upper()
        if user in gro:
            gro[user] += 1
        else:
            gro[user] = 1
        
    except  EOFError:
        sortG = sorted(gro)
        for i in sortG:
            print(f"{gro[i]} {i}")
        break
        