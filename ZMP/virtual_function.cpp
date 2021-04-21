#include <iostream>
#include <string>
using namespace std;

class Base {
public:
    virtual string getName(){
        return "Base";
    }

    int getLevel(){
        return 1;
    }
};

class Derived : public Base {
public:
    string getName() override {
        return "Derived";
    }

    int getLevel(){
        return 2;
    }
};

int main(){
    Base* p;
    Derived d;
    p= &d;
    cout << p->getName() << endl;
    cout << p->getLevel() << endl;
    return 0;
}