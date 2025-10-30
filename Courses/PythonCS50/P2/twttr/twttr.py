user = input("Input: ").strip()

vowels = ['a','e','i','o','u']
new = ""

for i in user.lower():
    if i not in vowels:
        new += i

print(f"Output: {new}")