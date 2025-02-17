
class Color:

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b


class Kettle:

    def __init__(self, brand, power=100, is_compatible_with_alice=False, color: Color='white'):
        # объем
        # фирма
        # мощьность
        # матиреал корпуса
        # срок службы
        # вид вилки
        # цвет
        # совместим с Алисой?
        # смарт?
        # размер
        self.brand = brand
        self.power = power
        self.is_compatible_with_alice = is_compatible_with_alice
        self.color = color
        self.is_switched = False
        self.temperature = 25

    # методы
    # включить выключить
    # набрать воды
    # вскипятить
    # подсветка
    # нагдеть до определнной температуры
    # подключить к алисе
    # сообщеить что вода скипела
    # включить режим бойлера

    def turn_on(self):
        self.is_switched = True

    def turn_off(self):
        self.is_switched = False

    def heat(self, new_temperature):
        while True:
            if self.temperature >= new_temperature:
                break
            self.temperature += 1
            print('current_temperature', self.temperature)


    def add_property(self):
        self.a = 10


white_kettle = Kettle(
    'Tefal'
)

red_kettle = Kettle(
    'Bork',
    color='Red',
)

print(
    white_kettle.is_switched
)

print(
    white_kettle.power
)

print(
    red_kettle.color
)

print('------------------------')

print(
    white_kettle.is_switched
)

white_kettle.turn_on()

print(
    white_kettle.is_switched
)

print(
    red_kettle.is_switched
)

red_kettle.add_property()
red_kettle.b = 20

red_kettle.heat(50)
red_kettle.heat(20)

strange_kettle = Kettle(
    'Strange brand',
    color=Color(56, 34, 34),
)

print(strange_kettle.color)