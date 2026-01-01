import csv

def updateRatings(ratings): # this is a list of dict objects with movie data
    try:
        with open("../data/my_ratings.csv",'w') as file: # remember "w" wipes the given file and starts fresh
            writer = csv.DictWriter(file, fieldnames=["movie_id","rating","timestamp"])
            writer.writeheader() #writes the headers, the given field names on top
            for row in ratings:
                writer.writerow(row) # since each is a dict, and csv expects dict, use the rows

    except FileNotFoundError:
        print("FileNotFoundError, maybe try again!")
