import json
from src.models.books import Book

class Database:
    def __init__(self, file_path: str = "library.json"):
        self.file_path = file_path
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                books_data = json.load(file)
                return [Book.from_dict(book) for book in books_data]
        except FileNotFoundError:
            return []

    def save_books(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, book: Book):
        self.books.append(book)
        self.save_books()

    def remove_book(self, book_id: int):
        self.books = [book for book in self.books if book.book_id != book_id]
        self.save_books()

    def search_books(self, **kwargs):
        results = self.books
        for key, value in kwargs.items():
            results = [book for book in results if getattr(book, key) == value]
        return results

    def update_status(self, book_id: int, new_status: str):
        for book in self.books:
            if book.book_id == book_id:
                book.status = new_status
                self.save_books()
                return
