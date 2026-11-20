class Classifier:

    def __init__(self):
        pass



class Book:

    # асбн классификатор
    # издательство
    # год издания
    # название
    # автор
    # переплет (твердая, мягкая)
    # количество страниц
    # отзывы критиков ?

    def __init__(self,
                 asbn_classifier,
                 brand,
                 publication_year,
                 name,
                 author,
                 cover_type,
                 page_count,
                 reviews,
                 ):
        self.asbn_classifier = asbn_classifier
        self.brand = brand
        self.publication_year = publication_year
        self.name = name
        self.author = author
        self.cover_type = cover_type
        self.page_count = page_count
        self.reviews=reviews

    # методы
    # продажа? (продать эту книгу)
    # доставка?
    # заказать?
    # почитать
    # вывести её описание
    # добавить отзыв о книге
    # сформировать описание

    def add_review(self, review):
        self.reviews.append(review)

    def create_description(self):
        return f'{self.name} {self.author} {len(self.reviews)}'

    def show_description(self):
        description = self.create_description()
        print(description)


