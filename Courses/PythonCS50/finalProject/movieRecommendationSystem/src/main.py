import read
import update
import sys

# helper module files

ratings = read.readRatings() # global vairable to store ratings data
movies = read.readMovies() # global variable to store movies data

def main():
    global ratings

    #print(read.readFile())
    #print(ratings)
    # ratings.append({
    #     "movieId": 3,
    #     "rating": 2,
    #     "timestamp": "2024-21-21"
    # })
    # update.updateRatings(ratings)

    menuInterface()

def menuInterface():
    print("1. View Movie Catalog")
    print("2. Rate A Movie")
    print("3. View My Ratings")
    print("4. Get Recommendations")
    print("5. Help")
    print("6. Exit")

    while True:
        try:
            choice = int(input("Enter a number: "))
            break
        except ValueError:
            print("Please enter a number from the given table!")

    match choice:
        case 1:
            viewCatalog()
        case 2:
            rateMovie()
        case 3:
            viewRatings()
        case 4:
            getRecommendations()
        case 5:
            getHelp()
        case 6:
            sys.exit("Exited Program")

def viewCatalog():
    pass
def rateMovie():
    pass
def viewRatings():
    pass
def getRecommendations():
    pass
def getHelp():
    pass















if __name__ == "__main__":
    main()