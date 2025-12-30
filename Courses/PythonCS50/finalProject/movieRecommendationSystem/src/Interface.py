import sys
from tabulate import tabulate

#prints the menu interface and interacts with other functions
def menuInterface(movies): 
    print("1. View Movie Catalog")
    print("2. Rate A Movie")
    print("3. View My Ratings")
    print("4. Get Recommendations")
    print("5. Help")
    print("6. Exit")

    while True:
        try: # scope is only under function and classes, try and while dont create their own scope, thus choice is usable all around the func
            choice = int(input("Enter a number: "))
            break
        except ValueError:
            print("Please enter a number from the given table!")

    match choice:
        case 1:
            viewCatalog(movies)
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

def viewCatalog(movies):
    counter = 0 # for indexes of movies
    tempMovies = [] # to store counter amout of movies

    while counter <= len(movies): # for as long as there are movies
        for i in range(10):
            tempMovies.append(movies[counter])
            if counter + 1 >= len(movies): # break if counter is become more or equal to movies, prevents index out of bounds
                break
            else:
                counter += 1

        print(tabulate(tempMovies, tablefmt="simple_grid")) # prints the given temp movies on a nice format

        print("-"*20 + "\n")
        print("1. More Movies")
        print("2. Main Menu")
        print("3. Help")
        print("4. Exit")

        # check for user options

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
    # go back to the main menu of there are no more movies to show
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
