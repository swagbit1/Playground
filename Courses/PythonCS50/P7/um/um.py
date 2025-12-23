import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    words = s.split(" ")
    count = 0
    for word in words:
        #match = re.search(r"^((?:.*)?um|um(?:.*)?)$",word)

        # Dont need to slplit and use loop when using for all
        match = re.findall(r"\bum\b", word) # this solution finds all um that are between non word characters, so accounts for ..um but not bum since b is a word character,.?! etc are not
        # splits the sentence into words and checks induvisualy since search only reutrns first occurance
        # checks if there is anything before or after um, which are optional. ie ....um.... or um... or ...um
        if match:
            count += 1
    
    return count





if __name__ == "__main__":
    main()