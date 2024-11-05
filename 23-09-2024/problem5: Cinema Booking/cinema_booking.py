# cinema_booking.py

# Dictionary to hold movie titles and their available seats
movies = {}

def add_movie(title, available_seats):
    """Adds a movie with the specified number of available seats."""
    movies[title] = available_seats

def book_seat(title):
    """Books a seat for the specified movie if available."""
    if title not in movies:
        return f"Movie '{title}' not found."
    if movies[title] > 0:
        movies[title] -= 1
        return f"Seat booked for '{title}'. Remaining seats: {movies[title]}"
    else:
        return f"No available seats for '{title}'."

def cancel_booking(title):
    """Cancels a booking for the specified movie."""
    if title not in movies:
        return f"Movie '{title}' not found."
    movies[title] += 1
    return f"Booking canceled for '{title}'. Available seats: {movies[title]}"

def check_available_seats(title):
    """Checks the number of available seats for the specified movie."""
    if title not in movies:
        return f"Movie '{title}' not found."
    return f"Available seats for '{title}': {movies[title]}"
