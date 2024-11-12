class Book:
    def __init__(self, title, author=None, year=None):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        title_str = f'{self.title:<30}'
        author_str = f'{self.author:<20}' if self.author else ' ' * 20
        year_str = f'{self.year:>5}' if self.year else ' ' * 5
        print(f'{title_str}{author_str}{year_str}')


class Library:
    def __init__(self, name, books=None):
        self.name = name
        self.books = books if books is not None else []

    def add_book(self, book):
        self.books.append(book)

    def delete_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def list(self):
        print(f'{"Название":<30}{"Автор":<20}{"Год":>5}')
        for book in self.books:
            book.display()

    def filter(self, title='', author='', year=None):
        filtered_books = []
        for book in self.books:
            title_match = title.lower() in book.title.lower() if title else True
            author_match = author.lower() in book.author.lower(
            ) if author and book.author else True
            year_match = (book.year == year) if year else True

            if title_match and author_match and year_match:
                filtered_books.append(book)

        return filtered_books

    @staticmethod
    def as_table(book_list):
        print(f'{"Название":<30}{"Автор":<20}{"Год":>5}')
        for book in book_list:
            book.display()


book_1 = Book('Война и мир', 'Лев Толстой', 1869)
book_2 = Book('Гарри Поттер', 'Дж. К. Роулинг', 1997)
book_3 = Book('Преступление и наказание', 'Федор Достоевский')
book_4 = Book('Маленький принц', year=1943)

library = Library('Библиотека')

library.add_book(book_1)
library.add_book(book_2)
library.add_book(book_3)
library.add_book(book_4)


library.list()


books = library.filter(author='Лев Толстой')
Library.as_table(books)
