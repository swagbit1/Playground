import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$",ip)
    # match that for ip adress #.#.#.# where each is a numnber between 0 and 255
    # checks if multiple numbers are from 0 to 9, 
    if match:
        # check if numbers are valid
        patterns = match.group().split(".")
        for p in patterns:
            if len(p) > 3:
                return False
            if int(p) > 255 or int(p) < 0:
                return False
            if p.startswith('0') and len(p) > 1:
                return False
    else:
        return False
    return True

if __name__ == "__main__":
    main()