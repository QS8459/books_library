from src.models.books import Book
class BookLibrary:
    def __init__(self, db):
        self.db = db
        self.next_id = max([book.book_id for book in db.books], default=0) + 1

    def add_book(self, title: str, author: str, year: int):
        book = Book(self.next_id, title, author, year)
        self.db.add_book(book)
        self.next_id += 1
        print(f"Книга добавлена: {book.title} ({book.author}, {book.year})")

    def remove_book(self, book_id: int):
        self.db.remove_book(book_id)
        print(f"Книга с id {book_id} удалена.")

    def list_books(self):
        books = self.db.books
        if not books:
            print("Библиотека пуста.")
        else:
            for book in books:
                print(f"{book.book_id}. {book.title} - {book.author} ({book.year}) [{book.status}]")

    def search_books(self, **kwargs):
        results = self.db.search_books(**kwargs)
        if not results:
            print("Ничего не найдено.")
        else:
            for book in results:
                print(f"{book.book_id}. {book.title} - {book.author} ({book.year}) [{book.status}]")
        return results

    def update_status(self, book_id: int, new_status: str):
        self.db.update_status(book_id, new_status)
        print(f"Статус книги с id {book_id} обновлен на {new_status}.")
