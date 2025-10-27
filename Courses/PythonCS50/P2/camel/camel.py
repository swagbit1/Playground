user = input("camelCase: ").strip()
new = ""

for i in user:
    if i >= 'A' and i <= 'Z':
        new += "_" + i
    
    else:
        new += i
    
print(f"snake_case: {new}")