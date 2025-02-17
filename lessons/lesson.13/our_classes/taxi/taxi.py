import time

class BabySeat:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Taxi:
    # свойство

    def __init__(self, tariff, color, driver, has_baby_seat=False, baby_seat=None):
        self.tariff = tariff
        self.color = color
        self.driver = driver
        self.has_baby_seat = has_baby_seat
        self.baby_seat = baby_seat

    # класс такси (эконом, бизнес)
    # цвет
    # номер
    # водитель
    # рейтинг
    # модель
    # тариф
    # число мест
    # деткское кресло
    # детское кресло бывает на разные возраста
    # объем багажника

    # Методы
    # забронировать/отменить

    def booking(self, user, time=time.time()):
        self.user = user
        self.booking_time = time

    # ожидание
    # отправить другому
    # позвонить водителю
    # помыть
    # использовать для курьерской доставки груза
    # сменить водителя

    def change_driver(self, new_driver):
        self.driver = new_driver

    # точка прибытия

econom_taxi = Taxi(
    tariff='econom',
    color='red',
    driver='Семён Семёныч',
)

business_taxi = Taxi(
    tariff='business',
    color='black',
    driver='Семён Семёныч',
    has_baby_seat=True,
    baby_seat=BabySeat(name='aaa', age=5)
)

print(econom_taxi.tariff)
print(business_taxi.tariff)

econom_taxi.tariff = 'classic'
print(econom_taxi.tariff)

econom_taxi.booking('Петрович', '372973')

print(econom_taxi.driver)

econom_taxi.change_driver('John Smith')

print(econom_taxi.driver)

# public, private, protected


class Category:
    pass


class Taxi:
    def __init__(self, categories = []):
        self.categories = categories