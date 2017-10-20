#include "controllerCPlusPlus.hpp"

controllerCPlusPlus::controllerCPlusPlus() {
}

void controllerCPlusPlus::keypadButton(char buttonValue) {
    
}

void controllerCPlusPlus::assignDrinkValues(char value) {
    if (userSelectLemonade == true) {
        userLemonadeValue += value;
    }
    else {
        userWaterValue += value;
    }
}