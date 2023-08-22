using System;

class Car {
    public string Make;
    public string Model;
    public int Year;
    public int Speed;

    public Car(string make, string model, int year) {
        Make = make;
        Model = model;
        Year = year;
        Speed = 0;
    }

    public void Accelerate(int increment) {
        Speed += increment;
    }

    public void Brake(int decrement) {
        Speed -= decrement;
    }

    static void Main(string[] args) {
        Car myCar = new Car("Toyota", "Corolla", 2023);
        Console.WriteLine($"My car: {myCar.Year} {myCar.Make} {myCar.Model}");

        myCar.Accelerate(20);
        Console.WriteLine($"Current speed: {myCar.Speed} mph");

        myCar.Brake(5);
        Console.WriteLine($"Current speed after braking: {myCar.Speed} mph");
    }
}
