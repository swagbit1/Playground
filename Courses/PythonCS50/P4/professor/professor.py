import random


def main():
    level = get_level()
    score = 0
    totalQ = 10
    while totalQ > 0:
        x = generate_integer(level)
        y = generate_integer(level)
        ans = x + y
        tries = 2

        print(f"{x} + {y} = ",end="")

        user = int(input())

        while user != ans and tries > 0:
            print("EEE")
            print(f"{x} + {y} = ", end="")
            user = int(input())
            tries -= 1
        
        if tries == 0:
            print(f"{x} + {y} = {ans}")
            print("NEW QUESTION")
            totalQ -= 1
        else:
            score += 1
            totalQ -= 1

    print(f"Score {score}/10")




def get_level():
    level = int(input("Level: "))

    while level < 0 or level > 3:
        level = int(input("Level: "))
    
    return level


def generate_integer(level):
    return int (random.random() * 10 ** level)

if __name__ == "__main__":
    main()