import unittest
from src.models.books import Book
from src.utils.database import Database
from src.book_library import BookLibrary

class TestBookLibrary(unittest.TestCase):

    def setUp(self):
        self.db = Database(file_path="test_library.json")
        self.library = BookLibrary(self.db)

    def tearDown(self):
        import os
        if os.path.exists("test_library.json"):
            os.remove("test_library.json")

    def test_add_book(self):
        self.library.add_book("Test Book", "Author", 2020)
        self.assertEqual(len(self.db.books), 1)
        self.assertEqual(self.db.books[0].title, "Test Book")

    def test_remove_book(self):
        self.library.add_book("Test Book", "Author", 2020)
        book_id = self.db.books[0].book_id
        self.library.remove_book(book_id)
        self.assertEqual(len(self.db.books), 0)

    def test_search_books(self):
        self.library.add_book("Test Book", "Author", 2020)
        results = self.library.search_books(title="Test Book")
        self.assertEqual(len(results), 1)

    def test_update_status(self):
        self.library.add_book("Test Book", "Author", 2020)
        book_id = self.db.books[0].book_id
        self.library.update_status(book_id, "выдана")
        self.assertEqual(self.db.books[0].status, "выдана")

if __name__ == "__main__":
    unittest.main()
