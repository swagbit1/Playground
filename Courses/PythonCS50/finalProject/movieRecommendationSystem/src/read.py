import csv

def readFile():
    try:
        with open("../data/movies.csv",'r') as file:
            return csv.DictReader(file)

    except FileNotFoundError:
        print("FileNotFoundError, maybe try again!")
