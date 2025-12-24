from datetime import date
from datetime import datetime
import inflect


def main():
    print(calculate(input("Date Of Birth: ")))



def calculate(userDate):

    p = inflect.engine()
    # inatialize the infelct libraby to use its functions

    today = date.today()
    #get the day of today 
    result = today - date.fromisoformat(userDate) # fromisoFormat converts string into a date format
    # subtracting two same type date results in deltaTime format 
    # in this format we can easily extract the number of days sinces passed

    minutes = result.days * 24 * 60

    return (p.number_to_words(minutes, andword="")).capitalize()
    # return the converted of minutes in words with 'and` word removed
    # 765 => seven hundren sixty five, very cool
if __name__ == "__main__":
    main()