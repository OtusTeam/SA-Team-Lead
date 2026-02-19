class Shop:

    def buy(self, user, toy):
        pass


class Repository:

    def crud(self, toy):
        pass


class FromToRange:

    def __init__(self, from_age, to_age):
        self.from_age = from_age
        self.to_age = to_age


class Toy:

    def __init__(
            self,
            toy_type: str,
            has_wheels: bool, # ? какие колеса
            material: str,
            from_age: FromToRange,
            sound: str = 'PPPEEEDDPEE!',
    ):
        # колеса
        # цвет
        # руль
        # материал
        # твердость
        # id ?
        # type
        # удалена или нет ?
        # для какого возраста
        self.toy_type = toy_type
        self.has_wheels = has_wheels
        self.material = material
        self.from_age = from_age
        self.sound = sound

    def save(self, db): # ?
        pass

    def buy(self, user):
        pass

    def make_sound(self):
        print(self.sound)
    # Методы
    # CRUD ?
    # ехать
    # летать
    # пищать
    # двигаться
    # Купить продать ?


class WheelToy(Toy):

    def drive(self, speed):
        pass


traktor = Toy(
    'Трактор',
    True,
    material='Файбер',
    from_age=FromToRange(5,10),
)

bear = Toy(
    'Медведь',
    False,
    material='Файбер',
    from_age=FromToRange(5,6),
    sound='Привет я медведь!'
)

traktor.make_sound()
bear.make_sound()
