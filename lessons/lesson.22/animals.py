
class Shop:

    def __init__(self, dogs):
        self.dogs = dogs

    def buy(self, dog):
        if dog in self.dogs:
            self.dogs.remove(dog)
            print('Вы купили собаку')
        else:
            print('Нет в магазине')

class Dog:

    # порода
    # цвет
    '''
    вес
    рост
    характер
    тип шерсти
    пол
    возраст
    цвет глаз
    имя
    '''

    def __init__(self, name, breed, character, fur_type, weight):
        self.name = name
        self.breed = breed
        self.character = character
        self.fur_type = fur_type
        self.weight = weight

    '''
    покормить
    выгулять
    лает
    багать
    лежать
    спать
    есть
    прыгать
    купить? - нет
    '''

    def wow(self):
        print('Wow wow')

    def feed(self, food, count):
        self.weight += count

    def __str__(self):
        return f'{self.name} {self.breed}'


little_dog = Dog(
    name='John',
    breed='Корги',
    character='Нордический',
    fur_type='Короткая',
    weight=2
)

big_dog = Dog(
    name='Maxin',
    breed='Хаски',
    character='Добрый',
    fur_type='Длинная',
    weight=10
)

other_dog = Dog(
    name='Maxin',
    breed='Хаски',
    character='Добрый',
    fur_type='Длинношерстная',
    weight=9
)

print(little_dog.name)
little_dog.wow()

print(big_dog)
big_dog.wow()

print(big_dog.weight)
big_dog.feed('meet', 4)
print(big_dog.weight)

shop = Shop([little_dog, big_dog, other_dog])

print('Buy:')
print(len(shop.dogs))
print(shop.dogs)

shop.buy(little_dog)

print(len(shop.dogs))
print(shop.dogs)