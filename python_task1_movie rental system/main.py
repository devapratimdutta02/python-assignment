from catalog import add_movie, display_movies
from rentals import rent_movie, return_movie
from earnings import calculate_earnings

add_movie("Avengers", "Action", 399)
add_movie("The Godfather", "Crime", 299)
add_movie("Toy Story", "Animation", 199)

while True:
    print("\n1. Display Movies")
    print("2. Rent Movie")
    print("3. Return Movie")
    print("4. Calculate Earnings")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        display_movies()
    elif choice == '2':
        customer_name = input("Enter customer name: ")
        movie_title = input("Enter movie title to rent: ")
        rent_movie(customer_name, movie_title)
    elif choice == '3':
        customer_name = input("Enter customer name: ")
        movie_title = input("Enter movie title to return: ")
        return_movie(customer_name, movie_title)
    elif choice == '4':
        calculate_earnings()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")