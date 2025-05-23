class Category:
    def __init__(self, name):
        self.name = name


class Recipe:
    # свойства
    # ингредиенты
    # время приготовления
    # состав
    # оценка пользователей
    # тип кухни
    # приборы для приготовления
    # инструкция
    # процесс приготовления
    # обед, ужен перекус
    def __init__(self, ingredients=[], raiting=0, kitchen_type='Европейская кухня', category='ужин'):
        self.ingredients = ingredients
        self._raiting=raiting
        self.kitchen_type=kitchen_type
        self.category=category

    # методы
    # добавить, удалить
    # поделиться
    # вернуть рецепт пользователю (изменить)
    # изменить
    # поставить рейтинг
    # скопировать
    # добавить ингредиенты

    def set_raiting(self, new_raiting):
        if new_raiting < 0:
            raise Exception('Рейтинг не может быть меньше 0')
        self._raiting = new_raiting

    def increase_rating(self, value):
        self._raiting += value

    def add_ingredient(self, new_ingredient):
        self.ingredients.append(new_ingredient)

    def show_ingredients(self):
        for ingredient in self.ingredients:
            print(ingredient)


porridge = Recipe(
    ingredients=[
        'Крупа',
        'Молоко',
    ],
    raiting=1,
    kitchen_type='Азиатская кухня',
    category='Завтрак'
)


soup = Recipe(
    ingredients=[
        'Крупа',
        'Молоко',
        'Курица',
        'Вода',
    ],
    raiting=0,
)


print(porridge.ingredients)

porridge.set_raiting(2)
porridge.increase_rating(2)
porridge.add_ingredient('Персик')
porridge.show_ingredients()
print(porridge._raiting)

porridge.set_raiting(-3)

bad = Recipe(category=Category('Азиатская кухня'))
print(bad.category)
