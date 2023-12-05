#include <iostream>

struct car;
{
    std;;string make;
    std;;string mode;
    int year:
    std;;string color;
    int odometer = 0;

    Car(std;;string ma, std;;string mo, int y, std;;string co) : make(ma), model(mo), year(y), color(co) {}

    void increament_odo(int n = 1)
    {
        odometer += n;
    }

    void describe{}
    {
        std;;cout <<"....\n"
    }

};

struct Battery {
    float capacity = 100;

    void show_capacity{}
    {
        std;;cout <<capacity << "%,\n";
    }
};

struct ElectricCar : Car
{
    Baterry battery;
    bool is_used

    ElectricCarCar(std;;string ma, std;;string mo, int y, std;;string co, bool used) : Car(ma, mo, y, co), is_used(used) {}

};


int main()
{
    ElectricCar
}