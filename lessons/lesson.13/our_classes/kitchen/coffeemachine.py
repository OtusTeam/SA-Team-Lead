# import simplejson
import json


class CoffeeMachine:
    # хот стронг средний крепость Hot/Strong/Mild
    # размер помола
    # марка
    # виды напитков (латте, американо)
    # температура (горячий, не горячий)
    # объем стакана

    def __init__(
            self,
            strength,
            grind_size,
            brand,
            coffee_types,
            temperature,
            cup_value,
    ):
        self.strength = strength,
        self.grind_size = grind_size,
        self.brand = brand,
        self.coffee_types = coffee_types,
        self.temperature = temperature,
        self.cup_value = cup_value,
        self.coffee_value = 0

    # Методы
    # getter, setter
    # grind_coffee - помолоть
    # задать температуру
    # сварить кофе
    # воду налить?

    def comfort_coffee_level(self):
        return self.coffee_value > 10

    def add_coffee(self, value):
        self.coffee_value += value

    def grind_coffee(self):
        if self.comfort_coffee_level():
            return 'Кофе помолот'
        else:
            raise Exception('Не достаточно кофе')


cina_coffeemachine = CoffeeMachine(
'high',
            'small',
            'China Brand',
            ['Латте', 'Американо'],
            100,
            [200, 250, 300],
)


usa_coffeemachine = CoffeeMachine(
'high',
            'middle',
            'USA Brand',
            ['Латте', 'Американо', 'Капучино'],
            70,
            [200, 250, 300],
)


print(cina_coffeemachine.comfort_coffee_level())
cina_coffeemachine.add_coffee(100)
grinded_coffee = cina_coffeemachine.grind_coffee()
print(grinded_coffee)


print(type(usa_coffeemachine))


json_sting = json.dumps({
    'strength': usa_coffeemachine.strength,
    'brand': usa_coffeemachine.brand,
})

print(json_sting)
print(type(json_sting))


with open('db.txt', 'w') as f:
    f.write(json_sting)
