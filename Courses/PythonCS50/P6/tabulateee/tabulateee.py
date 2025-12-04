from tabulate import tabulate
import sys


if len(sys.argv) < 2:
    sys.exit("Too few arguments")

userFile = sys.argv[1]

if not userFile.endswith(".csv"):
    sys.exit("Not CSV file")

try:
    with open(userFile) as file:
        temp = []
        for line in file:
            name,smallPrice, largePrice = line.rstrip().split(",")
            temp.append(list((name,smallPrice,largePrice)))

except FileNotFoundError:
    sys.exit("File not found")

print(tabulate(temp, tablefmt="grid"))