import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

if len(sys.argv) <= 2:
    user = input("Text: ")
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print(figlet.renderText(user))

else:
    if sys.argv[1] not in ["-f","--font"]:
        sys.exit()

    user = input("Text: ")
    
    
    f = sys.argv[2]
    print(f)
    figlet.setFont(font=f)
    print(figlet.renderText(user))

# run python3 figlet.py -f cosmic
        