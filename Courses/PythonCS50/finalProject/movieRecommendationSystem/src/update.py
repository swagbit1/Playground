import csv

def writeFile(movieId, rating, timestamp):
    try:
        with open("../data/my_ratings.csv",'w') as file:
            writer = csv.DictWriter(file, fieldnames=["movieId","rating","timestamp"])
            writer.writer({
                "movieId": movieId,
                "rating": rating,
                "timestamp": timestamp
            })
    except FileNotFoundError:
        print("FileNotFoundError, maybe try again!")
