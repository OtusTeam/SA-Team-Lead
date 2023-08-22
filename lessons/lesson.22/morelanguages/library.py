# Библиотеки Питера

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
        return self.book_list


child_library = Library(
    'some addres 1',
    '8912657898',
    ['золотая рыбка', 'буратино']
)

print(child_library.address)
child_library.change_adderess('other addres 3')
print(child_library.address)

print(child_library.get_book_list())

developer_library = Library(
    'main address',
    '90833837382',
    ['python', 'java']
)

print(developer_library.address)
developer_library.change_adderess('main address 2')
print(developer_library.address)

print(developer_library.get_book_list())

# print(developer_library.get_book_list('some argument'))
print(developer_library.get_book_by_name('python'))