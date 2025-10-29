def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # check first 2 are letters
    s1,s2 = s[0],s[1]

    if s1 < 'A' or s1 > 'Z' or s2 < 'A' or s2 > 'Z':
        return False
    
    if s[-1] >= 'A' and s[-1] <= 'Z':
        return False
    
    for i in s:
        if not ((i >= 'A' and i <= 'Z') or (i >= '0' and i <= '9')):
            return False
    
    return False if len(s) < 2 or len(s) > 6 else True


main()