import unittest
from src.utils.database import Database
from src.models.books import Book

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database(file_path="test_library.json")
        self.book = Book(book_id=1, title="Test Book", author="Author", year=2020)

    def tearDown(self):
        import os
        if os.path.exists("test_library.json"):
            os.remove("test_library.json")

    def test_add_book(self):
        self.db.add_book(self.book)
        self.assertEqual(len(self.db.books), 1)
        self.assertEqual(self.db.books[0].title, "Test Book")

    def test_remove_book(self):
        self.db.add_book(self.book)
        self.db.remove_book(self.book.book_id)
        self.assertEqual(len(self.db.books), 0)

    def test_search_books(self):
        self.db.add_book(self.book)
        results = self.db.search_books(title="Test Book")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Test Book")

    def test_update_status(self):
        self.db.add_book(self.book)
        self.db.update_status(self.book.book_id, "выдана")
        self.assertEqual(self.db.books[0].status, "выдана")

if __name__ == "__main__":
    unittest.main()
