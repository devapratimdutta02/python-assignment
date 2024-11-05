Here’s a challenging task that incorporates lists, tuples, dictionaries, functions, and modules in Python:

Task: Library Management System

You need to create a simple Library Management System that stores books and manages book loans. The system should handle book information, user details, and transactions (borrowing and returning books).

Requirements:

	1.	Books:
	•	Stored as a list of tuples, where each tuple contains:
	•	Book ID (integer)
	•	Book Title (string)
	•	Author (string)
	•	Number of copies available (integer)
	2.	Users:
	•	Stored in a dictionary, where each key is a unique User ID (integer) and the value is a tuple containing:
	•	User Name (string)
	•	A list of books borrowed by the user (as book IDs)
	3.	Functions:
	•	add_book(book_id, title, author, copies): Adds a new book to the system.
	•	register_user(user_id, user_name): Registers a new user.
	•	borrow_book(user_id, book_id): Allows a user to borrow a book if copies are available.
	•	return_book(user_id, book_id): Allows a user to return a book.
	•	view_books(): Displays all books in the library.
	•	view_user(user_id): Displays details of a specific user, including the books they have borrowed.
	4.	Module:
	•	Split the system into two files:
	•	library.py: Contains the core logic and functions.
	•	main.py: Where the interaction with the user takes place.
