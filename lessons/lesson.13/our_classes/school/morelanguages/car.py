class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, increment):
        self.speed += increment

    def brake(self, decrement):
        self.speed -= decrement

# Creating an instance of Car
my_car = Car("Toyota", "Corolla", 2023)
print(f"My car: {my_car.year} {my_car.make} {my_car.model}")

my_car.accelerate(20)
print(f"Current speed: {my_car.speed} mph")

my_car.brake(5)
print(f"Current speed after braking: {my_car.speed} mph")
