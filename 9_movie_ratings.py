def main():
    movie_ratings = {"About Time": 9,
                     "Scott Pilgrim vs. The World": 9,
                     "Morbius" : 2,
                     "The Great Gatsby": 7,
                     "Oppenheimer": 8}

    title = input("Please enter a movie title: ")

    recommend_movie(movie_ratings,title)

def recommend_movie(movie_ratings, movie_title):
    if movie_title in movie_ratings and movie_ratings[movie_title] >= 8:
            print("That's a great movie with great ratings! Definitely worth a watch.")
    else:
        print("Sorry! That movie is not recognized or below an 8/10 rating.\nHere are some movies with high ratings:")
        for movie in movie_ratings:
            if movie_ratings[movie] >= 8:
                print(movie)


main()