import read
import update

# helper module files

ratings = read.readRatings() # global vairable to store ratings data
movies = read.readMovies() # global variable to store movies data

def main():
    global ratings

    #print(read.readFile())
    print(ratings)
    ratings.append({
        "movieId": 3,
        "rating": 2,
        "timestamp": "2024-21-21"
    })
    update.updateRatings(ratings)













if __name__ == "__main__":
    main()