#include "controllerCPlusPlus.hpp"

controllerCPlusPlus::controllerCPlusPlus() {
}

controllerCPlusPlus::~controllerCPlusPlus() {
}

void controllerCPlusPlus::keypadButton(char buttonValue) {
    try {
        buttonActions[buttonValue]()
    } catch () {  }
}

