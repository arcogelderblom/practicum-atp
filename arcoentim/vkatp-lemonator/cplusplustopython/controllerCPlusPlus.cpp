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
    buttonActions['*'] = [&](){ hwInterface.attr("set")("isCupPresent", false); };
    buttonActions['#'] = [&](){ hwInterface.attr("set")("isCupPresent", true); };
    buttonActions['A'] = [&](){ userSelectLemonade = false; };
    buttonActions['B'] = [&](){ userSelectLemonade = true; };
    buttonActions['C'] = [&](){ userStartMixing = true; };
    buttonActions['D'] = [&](){ };
}

void controllerCPlusPlus::keypadButton(char buttonValue) {
    try {
        buttonActions[buttonValue]();
    } catch (...) {  }
}

void controllerCPlusPlus::assignDrinkValues(char value) {
    if (userSelectLemonade == true) {
        userLemonadeValue += value;
    }
    else {
        userWaterValue += value;
    }
}

void controllerCPlusPlus::updateLabels(void) {
    //Check for keypad input
    keypadButton(hwInterface.attr("getCKeypad")("keypad").cast<char>());
    
    //Check if a cup is in the machine
    if (!hwInterface.attr("get")("isCupPresent")) {
        hwInterface.attr("set")("sirupPump", 0);
        hwInterface.attr("set")("sirupValve", 1);
        hwInterface.attr("set")("waterPump", 0);
        hwInterface.attr("set")("waterValve", 1);
        hwInterface.attr("putString")("Put cup in machine");
    }
        
    //If the cup is present start checking some oter things
    else if (hwInterface.attr("get")("isCupPresent")) {
        if (userStartMixing) {
            if (originalDistanceSet) {
                currentLevel = originalDistance - hwInterface.attr("read_mm")().cast<int>();
            }
            else {
                originalDistance = hwInterface.attr("read_mm")().cast<int>();
                originalDistanceSet = true;
            }
                
            hwInterface.attr("putString")("Pouring your drink\nWater: " + userWaterValue + " Lemonade: " + userLemonadeValue);
            if (currentLevel < std::stoi(userLemonadeValue)) {
                hwInterface.attr("putString")("\nNow pouring: lemonade");
                hwInterface.attr("set")("sirupPump", 1);
                hwInterface.attr("set")("sirupValve", 0);
                hwInterface.attr("set")("waterPump", 0);
                hwInterface.attr("set")("waterValve", 1);
            }
                
            else if ((currentLevel >= std::stoi(userLemonadeValue)) && (currentLevel < std::stoi(userWaterValue) + std::stoi(userLemonadeValue))) {
                hwInterface.attr("set")("sirupPump", 0);
                hwInterface.attr("set")("sirupValve", 1);
                hwInterface.attr("set")("waterPump", 1);
                hwInterface.attr("set")("waterValve", 0);
                hwInterface.attr("putString")("\nNow pouring: water");
            }

            else {
                hwInterface.attr("set")("sirupPump", 0);
                hwInterface.attr("set")("sirupValve", 1);
                hwInterface.attr("set")("waterPump", 0);
                hwInterface.attr("set")("waterValve", 1);
                userStartMixing = false;
                userWaterValue = "0";
                userLemonadeValue = "0";
                hwInterface.attr("write_mm")(100);
                originalDistanceSet = false;
                currentLevel = 0;
            }
        }
        else if (!userStartMixing) {
            hwInterface.attr("set")("sirupPump", 0);
            hwInterface.attr("set")("sirupValve", 1);
            hwInterface.attr("set")("waterPump", 0);
            hwInterface.attr("set")("waterValve", 1);
            if (userSelectLemonade) {
                hwInterface.attr("putString")("Start(C)\nWater(A): " + userWaterValue + "\nLemonade(B): " + userLemonadeValue + "\nChange Lemonade");
            }
            else {
                hwInterface.attr("putString")("Start(C)\nWater(A): " + userWaterValue + "\nLemonade(B): " + userLemonadeValue + "\nChange Water");
            }
        }
    }
}