class Book:
    def __init__(self, title, Author=None, year=None):
        self.title = title
        self.Author = Author
        self.year = year

    def display(self):

        title_str = f'{self.title:<30}'

        author_str = f'{self.Author:<20}' if self.Author is not None else ''

        if self.Author is None and self.year is not None:
            year_str = f'{self.year:>25}'
        else:
            year_str = f'{self.year:>5}' if self.year is not None else ''

        print(f'{title_str}{author_str}{year_str}')


book1 = Book('Title', 'Author', 2020)
book1.display()

book2 = Book('Title', year=2020)
book2.display()

book3 = Book('Title', 'Author')
book3.display()
