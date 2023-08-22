# Библиотеки Питера

class Book:

    def __init__(self, name, author):
        self.name = name
        self.author = author


class Library:
    def __init__(self, address, telephone, book_list):
        # адрес
        self.address = address
        # телефон
        self.address = telephone
        # объем каталога
        # открыто/закрыто
        # руководитель
        # категория (детская не детская)
        # список книг
        self.book_list = book_list

    # открыть новую
    # закрыть существующиую
    # получить список книг
    def get_book_list(self):
        return self.book_list
    # обновить контактные данные
    def change_adderess(self, new_address):
        self.address = new_address
    # выдать книгу
    def get_book_by_name(self, name):
        pass

    def get_book_authors(self):
        result = []
        for book in self.book_list:
            result.append(book.author)
        return result


child_library = Library(
    'some addres 1',
    '8912657898',
    [
        Book('золотая рыбка', 'Пушкин'),
        Book('буратино', 'Толстой'),
    ]
)

print(child_library.get_book_authors())

