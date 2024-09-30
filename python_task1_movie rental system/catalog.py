movies = []

def add_movie(title, genre, rentalPrice):
    movie = (title, genre, rentalPrice)
    movies.append(movie)
    print(f"Added Movie: {movie}")

def display_movies():  # Updated function name
    if movies:
        print("Available movies:")
        for mov in movies:
            print(f"Title: {mov[0]}, Genre: {mov[1]}, Rental Price: {mov[2]}")
    else:
        print("No available movies.")

def get_movies():
    return movies
