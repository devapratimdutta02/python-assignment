import cinema_booking

cinema_booking.add_movie("Inception", 5)
cinema_booking.add_movie("The Matrix", 3)
cinema_booking.add_movie("Interstellar", 4)

print(cinema_booking.check_available_seats("Inception"))
print(cinema_booking.check_available_seats("The Matrix"))
    
print(cinema_booking.book_seat("Inception"))
print(cinema_booking.book_seat("The Matrix"))
    
print(cinema_booking.check_available_seats("Inception"))
print(cinema_booking.check_available_seats("The Matrix"))
    
print(cinema_booking.cancel_booking("Inception"))
    
print(cinema_booking.check_available_seats("Inception"))
