
class Shop:

    def __init__(self, dogs):
        self.dogs = dogs

    def show_dogs(self):
        print('*By our dogs:*')
        for dog in self.dogs:
            print(dog)

    def buy_a_dog(self, name):
        new_dogs = []
        result = None
        for dog in self.dogs:
            if dog.name == name:
                result = dog
            else:
                new_dogs.append(dog)
        self.dogs = new_dogs
        return result


class Dog:

    '''
    1. порода
    2. размер
    окрас
    вес
    пол
    характер
    имя
    '''
    def __init__(self, name, breed, size, color, character):
        self.name = name
        self.breed = breed
        self.size = size
        self.color = color
        self.character = character
        self.has_collar = False

    '''
    охранять
    подать голос
    бегать
    есть
    купит?
    спать
    '''

    def say(self):
        print('Wow wow!')

    def give_collar(self):
        self.has_collar = True

    def __str__(self):
        return f'{self.name}, {self.has_collar}'


little_dog = Dog(
    name='Tom',
    breed='Доберман',
    size=38,
    color='red',
    character='Bad',
)

big_dog = Dog(
    name='Джерри',
    breed='Водолаз',
    size=150,
    color='black',
    character='Good',
)

little_dog.say()
big_dog.say()

print(little_dog)
little_dog.give_collar()
print(little_dog)


shop = Shop(dogs=[little_dog, big_dog])

shop.show_dogs()

dog = shop.buy_a_dog('Джерри')
print(dog)

shop.show_dogs()
