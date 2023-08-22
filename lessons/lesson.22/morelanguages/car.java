public class Car {
    String make;
    String model;
    int year;
    int speed;

    public Car(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
        this.speed = 0;
    }

    public void accelerate(int increment) {
        speed += increment;
    }

    public void brake(int decrement) {
        speed -= decrement;
    }

    public static void main(String[] args) {
        Car myCar = new Car("Toyota", "Corolla", 2023);
        System.out.println("My car: " + myCar.year + " " + myCar.make + " " + myCar.model);

        myCar.accelerate(20);
        System.out.println("Current speed: " + myCar.speed + " mph");

        myCar.brake(5);
        System.out.println("Current speed after braking: " + myCar.speed + " mph");
    }
}
