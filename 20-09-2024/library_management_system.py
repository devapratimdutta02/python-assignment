books=[]
users={}

def add_book(book_id, title, author, copies):
    book=(book_id, title, author, copies)
    books.append(book)
    print(f"Book {title} added successfully.")
    
def register_user(user_id, user_name):
    if user_id in users:
        print(f"User {user_name} already registered.")
    else:
        users[user_id]=(user_name, [])
        print(f"User {user_name} registered successfully.")
        
def borrow_book(user_id, book_id):
    if user_id not in users:
        print(f"User ID {user_id} does not exist.")
        return
    
    for i, book in enumerate(books):
        if book[0] == book_id:
            if book[3] > 0:
                users[user_id][1].append(book_id)  
                books[i] = (book[0], book[1], book[2], book[3] - 1)
                print(f"Book '{book[1]}' borrowed by {users[user_id][0]}.")
                return
            else:
                print(f"Sorry, no copies of '{book[1]}' are available.")
                return

    print(f"Book with ID {book_id} not found.")