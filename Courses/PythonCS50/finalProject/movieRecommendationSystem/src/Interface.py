import sys
from tabulate import tabulate
import Update
import Read

movies = Read.readMovies()
ratings = Read.readRatings()

#prints the menu interface and interacts with other functions
def menuInterface(): 
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
    global movies
    global ratings
    # ensure the movie exists
    while True: # insure errors are handled for movie id
        try:
            id = int(input("Enter Id: "))
            while id < 1 or id > len(movies): # if movies has len 10, then index is 0-9, so if greater than index not count
                id = int(input("Enter Valid Id: "))
            break

        except ValueError:
            print("Invalid Input, Expecting A Different Type, Try Again!")

    curMovie = movies[id-1] # offset of index and getting the movie

    print(tabulate(curMovie.items(), tablefmt="simple_grid")) # getting the items from the dict and using tabulate to display movie
    print(f"Found this movie with id {id}")
    check = input("Confirm? [y/n]") # user confirmation of the movie
    if not 'n' in check:
        while True:
            try:
                userRating = float(input("Enter rating: "))

                if userRating < 0 or userRating > 5:
                    print("User Rating must be 0-5")
                else:
                    break

            except ValueError:
                print("Invalid Input, Try Again!")

        ratings.append({ # get the feedback from the user of thier prefrences and update it accordinlgy 
                            "movie_id": id,
                            "rating": userRating,
                            "timestamp": input("Enter Timestamp: ")              
                       })
        Update.updateRatings(ratings)
    else:
        print("Try Again! ")
    menuInterface()





def viewRatings():
    global ratings
    print(tabulate(ratings, headers='keys', tablefmt="simple_grid"))
    menuInterface()


def getRecommendations():
    global ratings
    global movies
    recommendations = set()
    genreCounter = {} # keys are genre, numbers are amount it appears
    watched = []
    watchedRating = []

    # get movies from id
    # check genres on it 
    # increase genre counter
    # have rating counter (number of time it appear) and rating sum -> finds average rating comedy -> [number of times it appears, sum rating each time, ]
    # this gets average rating
    # rank based on average rating

    #need all movies watched
    # recommend movie that is not watched
    for movie in ratings:
        id = int(movie["movie_id"])
        rating = movie["rating"]
        watched.append(movies[id - 1]) # get the movie id from rated movies and put them in watched list
        watchedRating.append([id,rating]) # keeps track of ratings for each watched movie with it's id
    
    for index, movie in enumerate(watched): # watched in now filled with movies.csv
        genres = movie["genres"].split(";") # genres is a given list so many
        for genre in genres:
            if genre in genreCounter: # if genre is alread in counter then
                genreCounter[genre][0] += 1 # increment it's count by 1
                genreCounter[genre][1] += float(watchedRating[index][1]) # add the sum of the ratings
            else:
                genreCounter[genre] = [1,float(watchedRating[index][1])] # if not then make it one and add it's current rating
    # above code arranges the watched movies with this format
    # {'Crime': [2, 6.5], 'Drama': [2, 6.5], 'Action': [1, 4.5]}
    # where left is the amout of time it appears and right is the sum of ratings, dividing latter by first gives avg
            
    """
        Average out the cumalitive ratings
    """
    for genre in genreCounter:
        totalApperance = genreCounter[genre][0]
        totalRating = genreCounter[genre][1]
        genreCounter[genre] = (totalRating / totalApperance)

    
    # this line sorts the given dictionary with regards to the values
    # dict meanas convert to dict
    # items gets it to (key,value)
    # lambda function takes item arg and returns item[1], key means how it is sorting
    # reverse means greatest to least
    # {'Action': 4.75, 'Crime': 3.5, 'Drama': 3.8, 'Sci-Fi': 4.5, 'Thriller': 3.5, 'Adventure': 5.0, 'Mystery': 4.0, 'Animation': 5.0}
    #{'Adventure': 5.0, 'Animation': 5.0, 'Action': 4.75, 'Sci-Fi': 4.5, 'Mystery': 4.0, 'Drama': 3.8, 'Crime': 3.5, 'Thriller': 3.5}
    genreCounter = dict(sorted(genreCounter.items(), key=lambda item: item[1], reverse=True))

    """
        Delete the last half of the keys so we get more rated ones
        {'Adventure': 5.0, 'Animation': 5.0, 'Action': 4.75, 'Sci-Fi': 4.5}
    """
    keys = list(genreCounter.keys())

    for i in keys[len(keys)//2:]: # removes from half till the end of keys
        del genreCounter[i]

    """
        Start recommending movies based on the genres and the difference in rating b
    """
    # go through the movies
    for movie in movies:
        DIFFERENCE = 0.3 # the abs difference between movie rating and your rating showed be this 
        if movie not in watched: #make sure the movie is not watched
            genres = movie["genres"].split(";") # get the genres
            movieAvgRating = movie["avg_rating"] # get the rating
            for genre in genres: # loop through each genres
                if genre in genreCounter: # if the genre in one of the ones from the user
                    if abs(float(movieAvgRating) - genreCounter[genre]) <= DIFFERENCE: # check the difference
                        recommendations.add(frozenset(movie.items())) # add it into a set so no dupes, set cannt accept dictonaries because they are mutable, so much use frozen to freeze them in place when adding to set
    print(tabulate([dict(x) for x in recommendations], tablefmt="simple_grid")) 
    # printout the movies using tabulate clean table format
    # using list comprehension to convert the frozen dict back into the dict format,
    # this ensured that no dupes was given in the recommendations
    print(genreCounter) # see your genres and how they are weighted


    # next goal is to use stronger recommendation system 





def getHelp():
    pass
