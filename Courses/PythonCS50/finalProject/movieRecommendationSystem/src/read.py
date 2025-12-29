import csv

# this file is responsible for reading the data
def readMovies():
    try:
        with open("../data/movies.csv",'r') as file:
            reader = csv.DictReader(file)
            movies = [] # list to put the read files as data will be lost with dict reader when it finishes

            for row in reader:
                movies.append(row)
            return movies # return the movies
    except FileNotFoundError:
        print("FileNotFoundError, maybe try again!")


def readRatings():
    try:
        with open("../data/my_ratings.csv","r") as file:
            reader = csv.DictReader(file)
            ratings = [] # to prevent loss of file data from dict reader, store it in this file

            for row in reader:
                ratings.append(row)
            return ratings
    except FileNotFoundError:
        print("FileNotFoundError, maybe try again!")


