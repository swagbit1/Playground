import sys


if (len(sys.argv)) < 2 or len(sys.argv) > 3:
    sys.exit("Arg less")

userFile = sys.argv[1]

if not userFile.endswith(".py"):
    sys.exit("Not py")

lines = 0
try:
    with open(userFile, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("#") or line == '':
                continue
            else:
                lines += 1

except FileNotFoundError:
    sys.exit("FIle not")

print(lines)