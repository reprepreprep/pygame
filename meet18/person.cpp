#include <iostream>
using namespace std;

struct person {
    string name = "budi"
    int age = 30;
    bool is_married = false;

    void say_hello(){
        cout << "Hello.....\n";
    }
}:

int main()
{
    Person person_1:
    cout << person_1.name << " 15 " << person_1.age << " years old now.\n";
    person_1.say_hello();
    return 0;
}