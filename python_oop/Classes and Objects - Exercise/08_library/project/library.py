from project.user import User


class Library:
    def __init__(self):
        self.user_records: list[User] = []
        self.books_available: dict[str, [str]] = {}
        self.rented_books: dict[str, dict[str, [int]]] = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name not in self.books_available[author]:
            days_left = 0
            for u, books in self.rented_books.items():
                if book_name in books:
                    days_left = books[book_name]
            return f'The book "{book_name}" is already rented and will be available in {days_left} days!'

        user.books.append(book_name)
        if user.username not in self.rented_books:
            self.rented_books[user.username] = {}
        self.rented_books[user.username][book_name] = days_to_return
        self.books_available[author].remove(book_name)
        return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"

        user.books.remove(book_name)
        self.books_available[author].append(book_name)
        del self.rented_books[user.username][book_name]
