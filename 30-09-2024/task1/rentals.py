from catalog import get_movies
from earnings import add_earning

rented_movies = {}

def rent_movie(customer_name, movie_title):
    available_movies = get_movies()
    
    for movie in available_movies:
        if movie[0] == movie_title:
            if customer_name not in rented_movies:
                rented_movies[customer_name] = []
            rented_movies[customer_name].append(movie)
            add_earning(movie[2])
            print(f"{customer_name} rented: {movie[0]}")
            return
            
    print("Movie not available.")

def return_movie(customer_name, movie_title):
    if customer_name in rented_movies:
        for movie in rented_movies[customer_name]:
            if movie[0] == movie_title:
                rented_movies[customer_name].remove(movie)
                print(f"{customer_name} returned: {movie[0]}")
                return
    print("Movie not rented by this customer.")

def display_rented_movies():
    if rented_movies:
        print("Rented Movies:")
        for customer, movies in rented_movies.items():
            movie_titles = ', '.join(movie[0] for movie in movies)
            print(f"{customer}: {movie_titles}")
    else:
        print("No movies rented.")