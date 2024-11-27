from src.models.books import Book
from src.utils.database import Database
from src.book_library import BookLibrary

def main():
    db = Database()
    library = BookLibrary(db)

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")
        choice = input("Введите номер действия: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания книги: "))
            library.add_book(title, author, year)
        elif choice == '2':
            book_id = int(input("Введите id книги для удаления: "))
            library.remove_book(book_id)
        elif choice == '3':
            criteria = input("Искать по (title/author/year): ")
            value = input("Введите значение для поиска: ")
            search_params = {criteria: value if criteria != "year" else int(value)}
            library.search_books(**search_params)
        elif choice == '4':
            library.list_books()
        elif choice == '5':
            book_id = int(input("Введите id книги для изменения статуса: "))
            new_status = input("Введите новый статус (в наличии/выдана): ")
            library.update_status(book_id, new_status)
        elif choice == '6':
            break
        else:
            print("Неверный выбор! Попробуйте снова.")

if __name__ == "__main__":
    main()
