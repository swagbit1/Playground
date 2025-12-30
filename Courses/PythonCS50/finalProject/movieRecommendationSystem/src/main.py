import read
import update
import sys
from tabulate import tabulate

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
    global movies
    counter = 0
    tempMovies = []

    while counter <= len(movies):
        for i in range(10):
            tempMovies.append(movies[counter])
            if counter + 1 >= len(movies):
                break
            else:
                counter += 1

        print(tabulate(tempMovies, tablefmt="simple_grid"))
        print("-"*20 + "\n")
        print("1. More Movies")
        print("2. Main Menu")
        print("3. Help")
        print("4. Exit")

        while True:
            try:
                choice = int(input("Enter A Number: "))
                break
            except ValueError:
                print("Please Enter A Given Choice Number From Above!")   

        match choice: #user can enter any other thing for more movies
            case 2:
                menuInterface()
            case 3:
                getHelp()
            case 4:
                sys.exit("Exited Program, Come again!")
        
        if counter == len(movies):
            break
    
    print("No More Movies To Go Through, Going Back To Main Menu! ")
    menuInterface()

                    




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