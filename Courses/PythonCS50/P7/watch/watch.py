import re
import sys

#http://youtube.com/embed/xvFZjo5PgG0
#https://youtube.com/embed/xvFZjo5PgG0
#https://www.youtube.com/embed/xvFZjo5PgG0

def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r"https?://(?:www\.)?youtube\.com/embed/([A-Za-z0-9_-]+)", s)
        # Cant do .+ as it checkes everything until new line, must do ^^^ for it to work and checkc properly
        # (?:) ignores it in the return groups as we dont care about it but also checks if www. is present or not
        # ? is optional one can do (http|https) to say one or the other, but more work but more readable

    if match:
        return f"https://youtu.be/{match.group(1)}"
    else:
        None


if __name__ == "__main__":
    main()