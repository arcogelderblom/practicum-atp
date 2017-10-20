#include "controllerCPlusPlus.hpp"

controllerCPlusPlus::controllerCPlusPlus() {
    buttonActions['1'] = [&](){ assignDrinkValues('1'); };
    buttonActions['2'] = [&](){ assignDrinkValues('2'); };
    buttonActions['3'] = [&](){ assignDrinkValues('3'); };
    buttonActions['4'] = [&](){ assignDrinkValues('4'); };
    buttonActions['5'] = [&](){ assignDrinkValues('5'); };
    buttonActions['6'] = [&](){ assignDrinkValues('6'); };
    buttonActions['7'] = [&](){ assignDrinkValues('7'); };
    buttonActions['8'] = [&](){ assignDrinkValues('8'); };
    buttonActions['9'] = [&](){ assignDrinkValues('9'); };
    buttonActions['0'] = [&](){ assignDrinkValues('0'); };
    buttonActions['*'] = [&](){ hwInterface.set("isCupPresent", false); };
    buttonActions['#'] = [&](){ hwInterface.set("isCupPresent", true); };
    buttonActions['A'] = [&](){ userSelectLemonade = false; };
    buttonActions['B'] = [&](){ userSelectLemonade = true; };
    buttonActions['C'] = [&](){ userStartMixing = true; };
    buttonActions['D'] = [&](){ };
}

controllerCPlusPlus::~controllerCPlusPlus() {
}

void controllerCPlusPlus::keypadButton(char buttonValue) {
    try {
        buttonActions[buttonValue]();
    } catch (...) {  }
}

