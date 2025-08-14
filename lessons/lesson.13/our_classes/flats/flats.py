class Person:

    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

    def get_name(self):
        return self._name


class Employer(Person):

    def calculate_salary(self):
        return 1002


class Flat:
    # свойства

    # площадь
    # кол-во комнат
    # адрес
    # комнатность
    # этаж
    # собственник
    # цена
    # ремонт
    def __init__(self, square, room_count, address, floor, owner: Person, price):
        self.square = square
        self.room_count = room_count
        self.address = address
        self.floor = floor
        self.owner = owner
        self.price = price
        self.is_rent = False
        self.currency = 'Руб'

    # методы
    # сдавать
    def rent(self):
        self.is_rent = True

    # купить, продать, аренда
    # объявление
    # жить
    # обновить данные
    def update_owner(self, new_owner):
        self.owner = new_owner

    # ремонтировать
    # оценить


old_flat = Flat(
    10,
    1,
    'Фадеева 12',
    5,
    Person('Leonid'),
    1200000
)

new_flat = Flat(
    100,
    4,
    'Фадеева 12',
    4,
    'Andrey',
    8200000
)

print(old_flat.owner)
old_flat.update_owner('Alex')

print(old_flat.owner)


class Home:

    def __init__(self, flats):
        self.flats = flats

    def total_price(self):
        result = 0
        for flat in self.flats:
            result += flat.price
        return result

home = Home([
    old_flat,
    new_flat
])

print(home.total_price())


employer = Employer('Макс')
print(employer.get_name())
print(employer.calculate_salary())


def plimorph(person: Person):
    print(person.get_name())


plimorph(Person('Leonid'))

plimorph(employer)
