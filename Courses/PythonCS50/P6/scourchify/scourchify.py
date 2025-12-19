import csv


with open("before.csv", 'r') as before, open("after.csv", 'w') as after:
    reader = csv.DictReader(before)
    writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for row in reader:
        last,first  = row["name"].strip().split(',')
        last = last.strip()
        first = first.strip()
        house = row["house"]
        writer.writerow({
            "first": first,
            "last": last,
            "house": house
        })