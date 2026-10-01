favorite_movies = [
    {"name": "Marley and Me", "year": 2008},
    {"name": "How to Lose a Guy in 10 Days", "year": 2003},
    {"name": "Zootopia", "year": 2016},
    {"name": "The Devil Wears Prada", "year": 2006},
    {"name": "The Parent Trap", "year": 1998}
]


def check_movie(movie):
    if movie["year"] < 2000:
        print("This movie was released before 2000")
    else:
        print("This movie was released after 2000")
        return movie["name"]
    
recent_movies = []
for movie in favorite_movies:
    returned_movie = check_movie(movie)

    if returned_movie is not None:
        recent_movies.append(returned_movie)


print(recent_movies)