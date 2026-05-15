from morelanguages.car import Car


class Person(Car, list):

    def __init__(self, name):
        self.name = name

    def say(self):
        print('Я человек')


class Student(Person):

    def __init__(self, name, age, car):
        self.name = name
        self.age = age
        self.car = car


class Group:
    # имя
    # номер
    # класс коррекции
    # кол-во человек
    # специализация
    # можской/женский
    def __init__(self, name, number, is_correction_class, specialization, gender):
        self.name = name
        self.number = number
        self.is_correction_class = is_correction_class
        self.specialization = specialization
        self.gender = gender
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def person_count(self):
        return len(self.students)

    def set_is_correction_class(self):
        self.is_correction_class = True

    def unset_is_correction_class(self):
        self.is_correction_class = False

    def full_name(self):
        return f'{self.number}{self.name}'


group_6a = Group(
    'A',
    6,
    False,
    'Математический',
    'M',
)
# response = input('Это класс коррекции?')
# if response == 'Да':
#     group.set_is_correction_class()
#     group.is_correction_class = True
# elif response == 'Нет':
#     group.unset_is_correction_class()

print(
    group_6a.full_name()
)

print(group_6a.is_correction_class)

group_7B = Group(
    'B',
    7,
    True,
    'Математический',
    'M',
)

print(group_7B.full_name())

print(group_7B.person_count())

group_7B.add_student('Коля')

group_7B.add_student(
    {'name': 'Николай', 'age': 30}
)

car = Car(
    'Лада',
    '9',
    1990,
)

student = Student(
    'Николай',
    30,
    car,
)

student.say()

group_7B.add_student(
    student
)

print(group_7B.person_count())



group_7B.students[-1].car.accelerate(1)

print(group_7B.students[-1].car.speed)