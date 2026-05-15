#include <iostream>
using namespace std;

class Car {
public:
    string make;
    string model;
    int year;
    int speed;

    Car(string make, string model, int year) {
        this->make = make;
        this->model = model;
        this->year = year;
        speed = 0;
    }

    void accelerate(int increment) {
        speed += increment;
    }

    void brake(int decrement) {
        speed -= decrement;
    }
};

int main() {
    Car myCar("Toyota", "Corolla", 2023);
    cout << "My car: " << myCar.year << " " << myCar.make << " " << myCar.model << endl;

    myCar.accelerate(20);
    cout << "Current speed: " << myCar.speed << " mph" << endl;

    myCar.brake(5);
    cout << "Current speed after braking: " << myCar.speed << " mph" << endl;

    return 0;
}
