def main():
    user = input("Input: ").strip()


def shorten(word):
    vowels = ['a','e','i','o','u']
    new = ""

    for i in word:
        if i.lower() not in vowels:
            new += i
    return new



if __name__ == "__main__":
    main()