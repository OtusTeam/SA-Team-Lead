class Point:
    def __init__(self, name, x, y):
        self.x = x
        self.y = y
        self.name = name


class Route:
    '''
    имя
    длина (км)
    клиентский номер ?
    день недели ?
    высота над уровнем моря
    начало - конец (пункты)
    время прохождения
    аэропорт вылета прилёта
    включен или отключен

    методы:
    включить
    транспорт?
    посчитать длину, время (на чем ехать)
    назначить транспорт
    сменить маршрут
    создать удалить
    купить билет
    добавить точку в маршрут
    '''

    def __init__(self, name, length, start: Point, end: Point, time: int):
        self.name = name
        self.length = length
        self.points = [start, end]
        self.time = time
        self.active = True

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def add_point(self, new_point):
        self.points.append(new_point)

    def points_count(self):
        return len(self.points)


moscov = Point('Москва', 23, 323)
petushki = Point('Петушки', 23, 3443)
piter = Point('Питер', 33, 2323)

moscov_petushki = Route(
    'Москва-Петушки',
    20,
    moscov,
    petushki,
    5,
)

moscov_piter = Route(
    'Москва-Питер',
    100,
    moscov,
    piter,
    15,
)

print(moscov_petushki.name)

print(moscov_petushki.points_count())

moscov_petushki.add_point(Point('Волгоград', 3434, 32323))

print(moscov_petushki.points_count())


print(moscov_petushki.points)
print(moscov_piter.points)