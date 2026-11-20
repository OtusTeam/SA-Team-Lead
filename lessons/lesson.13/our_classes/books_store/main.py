from books import Book
from shop import Shop


book1 = Book(
    '233-223-4455',
     'Гарант',
     1998,
     'Гарри Поттер и узник Азкабана',
     'Джоан Роллинг',
     'Мягкая', # ?
     200,
     ['Хорошая книга', 'Плохая книга'],
)


book2 = Book(
    '233-223-4455',
     'Гарант',
     1997,
     'Другая книга',
     'Другой автор',
     'idididididi', # ?
     200,
     ['Хорошая книга', 'Плохая книга'],
)


print(book1.cover_type)

book1.show_description()
book2.show_description()

book1.add_review('Нормальная книга')

book1.show_description()
print(book1.reviews)

shop = Shop(
    [book1, book2]
)

shop.sell(book1)


# book_data = [{...}]
# for data in book_data:
#     book = Book(**data)