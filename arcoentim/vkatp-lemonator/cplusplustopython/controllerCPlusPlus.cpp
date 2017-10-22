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
    keypadButton(hwInterface.getCKeypad("keypad"));
    
    //Check if a cup is in the machine
    if !hwInterface.get("isCupPresent"):
        hwInterface.set("sirupPump", 0)
        hwInterface.set("sirupValve", 1)
        hwInterface.set("waterPump", 0)
        hwInterface.set("waterValve", 1)
        hwInterface.putString("Put cup in machine")
        
    //If the cup is present start checking some oter things
    else if hwInterface.get("isCupPresent"):
        if userStartMixing:
            if originalDistanceSet:
                currentLevel = originalDistance - hwInterface.read_mm()
            else:
                originalDistance = hwInterface.read_mm()
                originalDistanceSet = true
                
            hwInterface.putString("Pouring your drink\nWater: " + std::itoa(std::stoi(userWaterValue))) + " Lemonade: " + std::itoa(std::stoi(userLemonadeValue)))
            if currentLevel < std::stoi(userLemonadeValue):
                hwInterface.putString("\nNow pouring: lemonade")
                hwInterface.set("sirupPump", 1)
                hwInterface.set("sirupValve", 0)
                hwInterface.set("waterPump", 0)
                hwInterface.set("waterValve", 1)
                
            else if currentLevel >= std::stoi(userLemonadeValue) and currentLevel < std::stoi(userWaterValue) + std::stoi(userLemonadeValue):
                hwInterface.set("sirupPump", 0)
                hwInterface.set("sirupValve", 1)
                hwInterface.set("waterPump", 1)
                hwInterface.set("waterValve", 0)
                hwInterface.putString("\nNow pouring: water")

            else:
                hwInterface.set("sirupPump", 0)
                hwInterface.set("sirupValve", 1)
                hwInterface.set("waterPump", 0)
                hwInterface.set("waterValve", 1)
                userStartMixing = false
                userWaterValue = "0"
                userLemonadeValue = "0"
                hwInterface.write_mm(100)
                originalDistanceSet = false
                currentLevel = 0

        else if !userStartMixing:
            hwInterface.set("sirupPump", 0)
            hwInterface.set("sirupValve", 1)
            hwInterface.set("waterPump", 0)
            hwInterface.set("waterValve", 1)
            if userSelectLemonade:
                hwInterface.putString("Start(C)\nWater(A): " + std::itoa(std::stoi(userWaterValue)) + "\nLemonade(B): " + std::itoa(std::stoi(userLemonadeValue)) + "\nChange Lemonade")
            else:
                hwInterface.putString("Start(C)\nWater(A): " + std::itoa(std::stoi(userWaterValue)) + "\nLemonade(B): " + std::itoa(std::stoi(userLemonadeValue)) + "\nChange Water")
}